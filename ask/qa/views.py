from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from .models import Question
from .forms import AskForm, AnswerForm, SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def paginate(request, query_set):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(query_set, 10)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def home(request):
    query_set = Question.objects.order_by('-id')
    page = paginate(request, query_set)
    return render(request, 'qa/home.html', {
        'page': page
    })


def question(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()
    if request.method == "POST":
        form = AnswerForm(initial={'question': question.id})
        form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AnswerForm()
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })


def popular(request):
    query_set = Question.objects.popular()
    page = paginate(request, query_set)
    return render(request, 'qa/popular.html', {
        'page': page
    })


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {'form': form})


def login_view(request):
    error = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = u'Wrong login or password!'
    form = SignupForm()
    return render(request, 'qa/login.html', {
        'form': form,
        'error': error,
    })
