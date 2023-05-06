from models.routesModel import routesModel

def handleGET(path):
    routesM = routesModel
    routes = routesM.routes

    try:
        file_name = routes[path]
        file = open(file_name, 'r')
    except (FileNotFoundError, KeyError):
        file = open("views/404.html", 'r')    

    message_body = file.read()
    file.close()

    return message_body