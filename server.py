import threading
from socket import *
import sys
import os

def threading_socket(connectionSocket):
    try:
        request = connectionSocket.recv(1024).decode()
        response = handle_request(request)
        connectionSocket.send(response.encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("File Not Found".encode())
        connectionSocket.close()

def handle_request(request):

    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html\r\n\r\n"
    message_body = handle_method(request)
    
    response = response_line+content_type+message_body
    return response

def handle_method(request):
    method = request.split()[0]
    path = request.split()[1]

    methods = {
        "GET": {
            "function": handle_GET,
            "params": (path)
        },
        "POST": {
            "function": handle_POST,
            "params": (request)
        }
    }

    try:
        method_handler = methods[method]
        return method_handler["function"](method_handler["params"])
    except KeyError:
        return "Method Not Allowed"

def handle_GET(path):
    path_dict = {
        "/": "index.html",
        "/files.html": "files.html"
    }

    try:
        file = open(path_dict[path], 'r')
    except (FileNotFoundError, KeyError):
        file = open("404.html", 'r')    

    message_body = file.read()
    file.close()

    return message_body

def handle_POST(request):
    search = request.split("\n")[25].replace("\r", "")
    file_pdf = """
    <div class="p-3">
        <i class="fa-solid fa-file-pdf" style="color: #c7c9cc;"></i>
        <h5 style="font-family: 'Comic Sans MS';">{}</h5>
    </div>
    """
    html_body = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">
            <script src="https://cdn.tailwindcss.com"></script>
            <title>Local Server</title>
            <style>
                input[type="text"],
                input[type="password"],
                textarea {
                    border: none;
                    outline: none;
                    border-bottom: 2px solid white;
            }
            </style>
        </head>
        <body style="background-color: #1a1a1a">
            <div class="flex flex-col items-center text-white">
                <div style="font-family: 'Comic Sans MS';" class="pt-20 text-4xl">
                    Kessoku Database
                </div>
                <div class="pt-10 px-10">
                    <form action="" method="POST" enctype="multipart/form-data">
                        <input type="text" id="searchFile" name="searchFile" style="background-color: #1a1a1a;" class="border-b-4" size="50">
                        <button type="Submit" class="ml-2 h-8 text-justify rounded-md p-1 bg-neutral-100 text-black">Search</button>
                    </form>
                </div>
                <div class="p-3 text-2xl" style="font-family: 'Comic Sans MS';">
                    Result Search for {}
                </div>
                <div class="p-5">
                </div>
                <div class="p-1 h-96 w-96">
                    <img src="https://i.ibb.co/gt4PXS7/member.jpg" alt="Member Kessoku">
                </div>
            </div>
        </body>
        </html>
    """
    files = os.listdir('./database')
    for name in files:
        if search in name:
            ...

            

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

