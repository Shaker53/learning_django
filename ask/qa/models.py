from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255, default='')
    text = models.TextField(default='')
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(null=True, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()

    def get_url(self):
        return reverse('question', args=[str(self.pk)])


class Answer(models.Model):
    text = models.TextField(default='')
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
