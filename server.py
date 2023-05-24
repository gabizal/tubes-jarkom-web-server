import threading
from socket import *
from handler.requestHandler import handleRequest
from models import Server

def threadingSocket(connectionSocket):
    try:
        request = connectionSocket.recv(1024).decode()
        response = handleRequest(request)
        connectionSocket.send(response.encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("File Not Found".encode())
        connectionSocket.close()

if __name__ == "__main__":
    server = Server(host='localhost', port=80, dir="views")
    
