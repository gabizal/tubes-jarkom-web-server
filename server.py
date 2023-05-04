import threading
from socket import *
import sys
import os

def threading_socket(connectionSocket):
    try:
        request = connectionSocket.recv(1024).decode()
        response = handle_request(request)
        connectionSocket.send(response.encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("File Not Found".encode())
        connectionSocket.close()

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

serverSocket = socket(AF_INET, SOCK_STREAM)
serverAddress = "localhost"
serverPort = 80

# reuse port
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind((serverAddress, serverPort))
serverSocket.listen(5)
#prepare server socket
print(f"\n\nYou can Acces Your Website in http://{serverAddress}:{serverPort}\n\n")
while True:
    connectionSocket, addr = serverSocket.accept()
    print(type(connectionSocket))
    threading.Thread(target=threading_socket, args=(connectionSocket,)).start()

