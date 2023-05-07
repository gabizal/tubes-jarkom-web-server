from models.routesModel import routesModel
from views.layouts.MainLayout import MainLayout
from views.layouts.HomePage import HomePage

def handleGET(path):
    # file = MainLayout(HomePage())
    
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
        file = open("views/404.html", 'r')
        content = file.read()
        file.close()
        return content