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