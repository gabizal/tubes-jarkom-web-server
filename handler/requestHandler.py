from handler.getHandler import handleGET
from handler.postHandler import handlePOST
from models.requestModel import Request
import datetime

def handleRequest(request: str) -> bytes:
    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html ; charset=utf-8\r\n"
    connection  = "COnnection: close\r\n"
    date = "Date: "+datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")+"\r\n"
    message_body: bytes = handleMethod(request)
    content_length = "Content-Length: "+str(len(message_body))+"\r\n\r\n"
    
    # response = response_line+content_type+connection+date+content_length+message_body
    response: bytes = message_body

    return response

def handleMethod(request) -> bytes:
    request = Request(request)

    if request.method == "GET":
        return handleGET(request.uri)
    elif request.method == "POST":
        return handlePOST(request.body)
    else:
        return "Method Not Allowed".encode()