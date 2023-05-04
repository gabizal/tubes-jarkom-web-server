import threading

def threading_socket(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        header = "HTTP/1.1 200 OK\nCOntent-Type: text/html\r\n\r\n"
        if filename[1:] == "/" or filename[1:] == "/index.html":
            message_body = open("index.html", 'r')
        connectionSocket.send(header.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("File Not Found".encode())
        connectionSocket.close()

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

