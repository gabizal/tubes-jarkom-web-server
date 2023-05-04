from handler.getHandler import *
from handler.postHandler import *

def handle_request(request):

    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html\r\n\r\n"
    message_body = handle_method(request)
    
    response = response_line+content_type+message_body
    return response

def handle_method(request):
    method = request.split()[0]
    path = request.split()[1]

    methods = {
        "GET": {
            "function": handle_GET,
            "params": (path)
        },
        "POST": {
            "function": handle_POST,
            "params": (request)
        }
    }

    try:
        method_handler = methods[method]
        return method_handler["function"](method_handler["params"])
    except KeyError:
        return "Method Not Allowed"  