from os import listdir
from views.layouts.FilePage import FilePage
from views.layouts.HomePage import HomePage
from views.MainLayout import MainLayout
from views.layouts.page404 import page404


class Routes:
    def __init__(self):
        self.routes = {
            "/": (MainLayout, HomePage),
            "/files": (MainLayout, FilePage),
            "/404": (MainLayout, page404),
        }

        self.updateFile()
    
    def updateFile(self):
        for file in listdir("database"):
            self.routes["/database/"+file] = "database/"+file
    
routesModel = Routes()