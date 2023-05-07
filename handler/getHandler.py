from models.routesModel import routesModel

def handleGET(path):
    routesM = routesModel
    routes = routesM.routes

    try:
        page = routes[path]
        if type(page) == tuple:
            content = page[0](page[1]())
        else:
            file = open(page, 'r')
            content = file.read()
            file.close()
        return content
    except (FileNotFoundError, KeyError):
        page = routesM.routes["/404"]
        content = page[0](page[1]())
        return content