from handler.getHandler import *
from handler.postHandler import *

def handleRequest(request):

    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html\r\n\r\n"
    message_body = handleMethod(request)
    
    response = response_line+content_type+message_body
    return response

def handleMethod(request):
    method = request.split()[0]
    path = request.split()[1]

    methods = {
        "GET": {
            "function": handleGET,
            "params": (path)
        },
        "POST": {
            "function": handlePOST,
            "params": (request)
        }
    }

    try:
        method_handler = methods[method]
        return method_handler["function"](method_handler["params"])
    except KeyError:
        return "Method Not Allowed"  