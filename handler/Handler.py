import os
from models import Request, Response
from views import HomePage, FilePage


class Handler:
    """Class untuk menghandle request dari client"""
    @staticmethod # Static method agar tidak perlu membuat instance
    def HomePage(request: Request):
        return Response.fromText(HomePage()) # Mengirim response berupa html

    @staticmethod
    def SearchPage(request: Request):
        searchKey: str = request.body["value"] # Mengambil value dari body

        files = os.listdir("database") # Membaca isi direktori database

        result = [] # List untuk menyimpan nama file yang sesuai dengan pencarian
        for name in files:
            if searchKey.lower() in name.lower():
                result.append(name) # Menambahkan nama file ke list result

        return Response.fromText(FilePage(files=result, search=searchKey)) # Mengirim response berupa html
