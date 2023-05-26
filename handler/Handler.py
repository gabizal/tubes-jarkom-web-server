import os
from models import Request, Response
from views import HomePage, FilePage


class Handler:
    @staticmethod
    def HomePage(request: Request):
        return Response.fromText(HomePage())

    @staticmethod
    def SearchPage(request: Request):
        searchKey: str = request.body["value"]

        files = os.listdir("database")

        result = []
        for name in files:
            if searchKey.lower() in name.lower():
                result.append(name)

        return Response.fromText(FilePage(files=result, search=searchKey))
