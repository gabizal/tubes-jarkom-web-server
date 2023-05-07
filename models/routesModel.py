from os import listdir
from views.layouts.HomePage import HomePage
from views.layouts.MainLayout import MainLayout


class Routes:
    def __init__(self):
        self.routes = {
            "/": (MainLayout, HomePage),
            "/files.html": (MainLayout, HomePage),
        }

        self.updateFile()
    
    def updateFile(self):
        for file in listdir("database"):
            self.routes["/database/"+file] = "database/"+file
    
routesModel = Routes()