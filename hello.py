def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])

    query_string_list = environ['QUERY_STRING'].split('&')
    query_string_bytes = bytes('\r\n'.join(query_string_list), encoding="utf8")
    return [query_string_bytes]
