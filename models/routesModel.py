from os import listdir

class Routes:
    def __init__(self):
        self.routes = {
            "/": "views/index.html",
            "/index.html": "views/index.html",
            "/files.html": "views/files.html",
        }

        self.updateFile()
    
    def updateFile(self):
        for file in listdir("database"):
            self.routes["/database/"+file] = "database/"+file
    
routesModel = Routes()