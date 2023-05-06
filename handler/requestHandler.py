from handler.getHandler import handleGET
from handler.postHandler import handlePOST
from models.requestModel import Request

def handleRequest(request):
    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html ; charset=utf-8\r\n\r\n"
    message_body = handleMethod(request)
    
    response = response_line+content_type+message_body
    return response

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