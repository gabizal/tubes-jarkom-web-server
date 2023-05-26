import threading, socket, os

from models import Request, Response


class Server:
    def __init__(self, host, port, rootDir="database"):
        self.host = host
        self.port = port
        self.server = None
        self.maxConnections = 1
        self.maxRecv = 4096
        self.rootDir = rootDir
        self.routes = {}

    def run(self):
        """Running socket server"""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(self.maxConnections)

        print(f"Server is running on http://{self.host}:{self.port}")

        while True:
            clientConnection = self.server.accept()
            threading.Thread(
                target=self.connectionHandler,
                args=clientConnection,
            ).start()

    def connectionHandler(self, clientSock, clientAddr):
        """Client connection's handler"""
        with clientSock:
            clientRequest = clientSock.recv(self.maxRecv).decode()
            if clientRequest:
                clientSock.sendall(self.handleRequest(clientAddr, clientRequest))

    def addRoute(self, path, handler):
        """Add custom route and handler"""
        self.routes[path] = handler

    def handleRequest(self, addr, request):
        """Handling request data from client"""
        request = Request(request)

        print(f"{addr}: {request.method=}, {request.path=}")

        if request.path in self.routes:
            return self.routes[request.path](request)

        fileName = request.path.split("/file/")[-1]
        files = os.listdir(self.rootDir)
        if fileName in files:
            return bytes(Response.fromFile(self.rootDir + "/" + fileName))

        return Response.errorResponse()
