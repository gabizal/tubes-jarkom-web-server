import threading
from socket import *
from handler.getHandler import *
from handler.postHandler import *
from handler.requestHandler import *

def threading_socket(connectionSocket):
    try:
        request = connectionSocket.recv(1024).decode()
        response = handle_request(request)
        connectionSocket.send(response.encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("File Not Found".encode())
        connectionSocket.close()

if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverAddress = "localhost"
    serverPort = 80

    # reuse port
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    serverSocket.bind((serverAddress, serverPort))
    serverSocket.listen(5)
    #prepare server socket
    print(f"\n\nYou can Acces Your Website in http://{serverAddress}:{serverPort}\n\n")
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(type(connectionSocket))
        threading.Thread(target=threading_socket, args=(connectionSocket,)).start()

