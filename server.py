import threading
from socket import *
import sys
import os
# 25
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
    if method == "GET":
        return handle_GET(path)
    elif method == "POST":
        return handle_POST(request)
    else:
        ...

def handle_GET(path):
    if path == "/" or path == "/index.html":
        file = open("index.html", 'r')
        message_body = file.read()
        file.close()
    elif path == "/files.html":
        ...
    else:
        file = open("404.html", 'r')
        message_body = file.read()
        file.close()
    return message_body

def handle_POST(request):
    form_search = request.split("\n")[25]
    return os.listdir('./database')[0]

serverSocket = socket(AF_INET, SOCK_STREAM)
serverAddress = "localhost"
serverPort = 80
serverSocket.bind((serverAddress, serverPort))
serverSocket.listen(5)
#prepare server socket
print(f"\n\nYou can Acces Your Website in http://{serverAddress}:{serverPort}\n\n")
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=threading_socket, args=(connectionSocket,)).start()
    
serverSocket.close()
sys.exit()

