# import threading
# from socket import *
# from handler.requestHandler import handleRequest

# def threadingSocket(connectionSocket):
#     try:
#         request = connectionSocket.recv(1024).decode()
#         response = handleRequest(request)
#         connectionSocket.send(response.encode())
#         connectionSocket.close()
#     except IOError:
#         connectionSocket.send("File Not Found".encode())
#         connectionSocket.close()

# if __name__ == "__main__":
#     serverSocket = socket(AF_INET, SOCK_STREAM)
#     serverAddress = "localhost"
#     serverPort = 80

#     # reuse port
#     serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#     serverSocket.bind((serverAddress, serverPort))
#     serverSocket.listen(5)

#     #prepare server socket
#     print(f"\n\nYou can Acces Your Website in http://{serverAddress}:{serverPort}\n\n")

#     # server loop
#     while True:
#         connectionSocket, addr = serverSocket.accept()
#         threading.Thread(target=threadingSocket, args=(connectionSocket,)).start()


import os
from models.Request import Request
from models.Response import Response
from models.Server import Server
from views.layouts.FilePage import FilePage
from views.layouts.HomePage import HomePage


def HomePageHandler(request: Request):
    return bytes(Response.fromText(HomePage()))


def SearchPageHandler(request: Request):
    searchKey: str = request.body["value"]
    print(searchKey, len(searchKey))
    result = []
    files = os.listdir("database")
    print(files)
    for name in files:
        if searchKey.lower() in name.lower():
            result.append(name)
    return bytes(Response.fromText(FilePage(files=result, search=searchKey)))


server = Server("localhost", 80)
server.addRoute("/", HomePageHandler)
server.addRoute("/search", SearchPageHandler)
server.run()
