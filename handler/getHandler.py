import os

def handleGET(path):
    path_dict = {
        "/": "views/index.html",
        "/index.html": "views/index.html",
        "/files.html": "views/files.html",
    }

    for file in os.listdir("database"):
        path_dict["/database/"+file] = "database/"+file

    try:
        file_name = path_dict[path]
        file = open(file_name, 'r')
    except (FileNotFoundError, KeyError):
        file = open("views/404.html", 'r')    

    message_body = file.read()
    file.close()

    return message_body