from models.routesModel import routesModel

def handleGET(path):
    routesM = routesModel
    routes = routesM.routes

    try:
        page = routes[path]
        file = page[0](page[1]())
        # file = open(file_name, 'r')
    except (FileNotFoundError, KeyError):
        file = open("views/404.html", 'r')    

    # message_body = file.read()
    # file.close()

    return str(file)