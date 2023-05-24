import threading, os, re
from socket import *

class Server:
    def __init__(self, host, port, dir="./"):
        self.host = host
        self.port = port
        self.server = None
        self.maxConnections = 5
        self.maxRecv = 4096
        self.rootDir = dir
        self.routes = {}

    def run(self):
        """Running socket server"""
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(self.maxConnections)

        # Display server info
        print(f"\n\nYou can Acces Your Website in http://{serverAddress}:{serverPort}\n\n")

        while True:
            clientSocket, clientAddr = self.server.accept()
            threading.Thread(target=self.connectionHandler,
                             args=(clientSocket, clientAddr)
                             ).start()
    
    def connectionHandler(self, clientSocket, clientAddr):
        """Client connection's handler"""
        with clientSocket:
            clientRequest = clientSocket.recv(self.maxRecv).decode()
            if clientRequest:
                clientSocket.sendall(
                    self.connectionHandler(clientAddr, clientRequest)
                )
    
    


