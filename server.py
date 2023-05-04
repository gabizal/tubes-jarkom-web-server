import threading

def threading_socket(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        response = handle_request(filename)
        connectionSocket.send(response.encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("File Not Found".encode())
        connectionSocket.close()

def handle_request(filename):
    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html\r\n\r\n"
    print(filename[0])
    if filename[0] == "/" or filename[0] == "/index.html":
        file = open("index.html", 'r')
    else:
        file = open("404.html", 'r')
    message_body = file.read()
    file.close()
    response = response_line+content_type+message_body
    return response

def handle_method(method):
    if method == "GET":
        ...
    elif method == "POST":
        ...
    else:
        ...

from socket import *
import sys
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

