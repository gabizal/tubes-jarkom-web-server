import os
from views.layouts.FilePage import FilePage
from views.MainLayout import MainLayout

def handlePOST(request_body: str) -> bytes:
    search = request_body.split("value=")[1].replace("\r", "").replace("\n", "")
    
    result = []
    files = os.listdir('./database')
    for name in files:
        if search.lower() in name.lower():
            result.append(name)
   
    page = MainLayout(FilePage(search, result)).encode()
    return page
