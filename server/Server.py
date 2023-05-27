import threading, socket, os, time, random

from models import Request, Response


class Server:
    
    def __init__(self, host, port, rootDir="database"):
        """Initialize server"""
        self.host = host
        self.port = port
        self.server = None
        self.maxConnections = 1
        self.maxRecv = 4096
        self.rootDir = rootDir
        self.routes = {}

    def run(self):
        """Running socket server"""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Penggunaan ulang port
        self.server.bind((self.host, self.port)) # Binding host dan port
        self.server.listen(self.maxConnections) # Listen for incoming connections

        print(f"\nServer is running on http://{self.host}:{self.port}\n\n")

        while True:
            clientConnection = self.server.accept() # Menerima koneksi dari client
            threading.Thread(
                target=self.connectionHandler,
                args=clientConnection,
            ).start() # Menjalankan thread untuk menghandle koneksi dari client

    def connectionHandler(self, clientSock, clientAddr):
        """Client connection's handler"""
        with clientSock: # Menutup socket client setelah selesai
            clientRequest = clientSock.recv(self.maxRecv).decode() # Menerima request dari client
            if clientRequest: 
                clientSock.sendall(self.handleRequest(clientAddr, clientRequest)) # Mengirim response ke client

    def addRoute(self, path: str, handler: callable):
        """Add custom route and handler"""
        self.routes[path] = handler # Menambahkan route ke dictionary routes

    def handleRequest(self, addr, request):
        """Handling request data from client"""
        request = Request(request) # Membuat objek request dari data request client

        """Menambahkan delay untuk Test Multi-Threaded"""
        randomTime = random.randint(1, 5)
        time.sleep(randomTime) # Menambahkan delay untuk simulasi
        print(f"Client {{{addr[0]}:{addr[1]} | method='{request.method}', path='{request.path}', Time Delay = {randomTime}s}}")

        if request.path in self.routes:
            return self.routes[request.path](request) # Menjalankan handler dari route yang diminta

        fileName = request.path.split("/file/")[-1] # Mengambil nama file dari path
        fileName = fileName.replace("%20", " ")  # Mengganti %20 dengan spasi
        files = os.listdir(self.rootDir) # Membaca isi direktori database
        if fileName in files:
            return bytes(Response.fromFile(self.rootDir + "/" + fileName)) # Mengirim file ke client

        return Response.errorResponse()
