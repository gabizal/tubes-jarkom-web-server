import threading
import socket

from models.Request import Request
from models.Response import Response

import threading, socket, os, re


class Server:
    def __init__(self, host, port, rootDir="database"):
        self.host = host  # Hostname or IP address
        self.port = port  # Port number
        self.server = None  # Server socket object
        self.maxConnections = 1  # Max connections
        self.maxRecv = 4096  # Max receive data size
        self.rootDir = rootDir  # Root directory for static files
        self.routes = {}  # Routes dict for custom routes and handlers

    def run(self):
        """Running socket server"""
        self.server = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )  # Create a socket object (TCP)
        self.server.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
        )  # Prevent socket.error: [Errno 48] Address already in use
        self.server.bind((self.host, self.port))  # Bind to the server host and port
        self.server.listen(self.maxConnections)  # Now wait for client connection.

        # Display server info to console
        print(f"Server is running on http://{self.host}:{self.port}")

        # Server's main loop (infinite loop)
        while True:
            clientConnection = self.server.accept()
            threading.Thread(
                target=self.connectionHandler,  # Start a new thread for handle client's request by calling
                args=clientConnection,  # connectionHandler method with clientSock and clientAddr as arguments
            ).start()

    def connectionHandler(self, clientSock, clientAddr):
        """Client connection's handler"""
        with clientSock:  # Close socket when done (`with` statement)
            clientRequest = clientSock.recv(
                self.maxRecv
            ).decode()  # Receive request from client
            if (
                clientRequest
            ):  # If client request is not empty (client request is exist)
                clientSock.sendall(
                    self.handleRequest(
                        clientAddr, clientRequest
                    )  # Send all response to client by calling handleRequest method client's attribute as arguments
                )

    def addRoute(self, path, handler):
        """Add custom route and handler"""
        self.routes[
            path
        ] = handler  # Add route and handler to routes dict (path as key, handler as value)

    def handleRequest(self, addr, request):
        """Handling request data from client"""
        request = Request(request)  # Parse raw request data to Request object

        print(
            f"{addr}: {request.method=}, {request.path=}"
        )  # Display request info to console

        if request.path in self.routes:
            return self.routes[request.path](request)

        fileName = request.path.split("/file/")[-1]
        files = os.listdir(self.rootDir)
        print(fileName)
        print(files)
        if fileName in files:
            return bytes(Response.fromFile(self.rootDir + "/" + fileName))

        return Response.errorResponse()
