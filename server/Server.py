import threading, socket, os, time, random

from models import Request, Response

# clientCount = 1


class Server:
    def __init__(self, host, port, rootDir="database"):
        """Initialize server"""
        self.host = host  # Server hotname or ip. example "localhost"
        self.port = port  # Server port. example "80" for http
        self.server = None  # Server variable to store socket
        self.maxConnections = 1  # Number of maximum connections
        self.maxRecv = 4096  # Number of maximum bytes received
        self.rootDir = rootDir  # Root folder for file
        self.routes = {}  # Routes dictionay added by addRoute(...)

    def run(self):
        """Running socket server"""
        self.server = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )  # Create socket using IPv4, TCP
        self.server.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
        )  # Reuse socket address
        self.server.listen(self.maxConnections)  # Listen for incoming connections

        # Print server info
        print(f"\nServer is running on http://{self.host}:{self.port}\n\n")

        # Server loop
        while True:
            clientConnection = self.server.accept()  # Create client connection
            threading.Thread(
                target=self.connectionHandler,
                args=clientConnection,
            ).start()  # Thread to handle multiple connections

    def connectionHandler(self, clientSock, clientAddr):
        """Client connection's handler"""
        with clientSock:  # Auto close socket
            clientRequest = clientSock.recv(
                self.maxRecv
            ).decode()  # Receive request from client
            if clientRequest:
                clientSock.sendall(
                    self.handleRequest(clientAddr, clientRequest)  # Handle request
                )  # Send response to client

    def addRoute(self, path: str, handler: callable):
        """Add custom route and handler"""
        self.routes[path] = handler  # Add route to routes dictionary

    def handleRequest(self, addr, request):
        """Handling request data from client"""
        request = Request(request)  # Parsing request data to Request object

        # Print request info
        print(f"{addr}: {request.method=}, {request.path=}")

        """
        #Menambahkan delay untuk Test Multi-Threaded#
        global clientCount
        randomTime = random.randint(1, 5)
        time.sleep(randomTime) # Menambahkan delay untuk simulasi
        print(f"Client {clientCount} {{{addr[0]}:{addr[1]} | method='{request.method}', path='{request.path}', Time Delay = {randomTime}s}}")
        clientCount += 1
        """

        # Look for route handler
        if request.path in self.routes:
            return self.routes[request.path](
                request
            )  # Call handler function and return response

        # If route not found, look for file in database
        fileName = request.path.split("/file/")[-1]  # Get file name from path
        fileName = fileName.replace("%20", " ")  # Replace %20 with space
        files = os.listdir(self.rootDir)  # Get all files in database

        # If file found, send file to client
        if fileName in files:
            return bytes(  # Convert to bytes
                Response.fromFile(
                    self.rootDir + "/" + fileName
                )  # Create response from file
            )  # Return file response

        # If rote and file not found, return error response
        return Response.errorResponse()
