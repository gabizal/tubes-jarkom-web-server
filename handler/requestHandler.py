from handler.getHandler import *
from handler.postHandler import *

def handleRequest(request):

    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html ; charset=utf-8\r\n\r\n"
    message_body = handleMethod(request)
    
    response = response_line+content_type+message_body
    return response

class Request:
    def __init__(self, decodedRequest: str):
        request = ''.join((line + '\n') for line in decodedRequest.splitlines())
        request_head, request_body = request.split('\n\n', 1)

        request_head = request_head.splitlines()
        request_headline = request_head[0]
        request_headers = dict(x.split(': ', 1) for x in request_head[1:])
        request_method, request_uri, request_proto = request_headline.split(' ', 3)

        self.method = request_method
        self.uri = request_uri
        self.proto = request_proto
        self.body = request_body
        self.headers = request_headers

def handleMethod(request):
    request = Request(request)

    # method = request.split()[0]
    # path = request.split()[1]
    if request.method == "GET":
        return handleGET(request.uri)
    elif request.method == "POST":
        return handlePOST(request.body)
    else:
        return "Method Not Allowed"