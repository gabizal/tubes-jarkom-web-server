import os
from handler.messageHandler import *
from views.layouts.FilePage import FilePage

def handlePOST(request_body: str):
    print(request_body)
    search = request_body.split("value=")[1].replace("\r", "").replace("\n", "")
    print(search)
    result = []
    files = os.listdir('./database')
    for name in files:
        if search.lower() in name.lower():
            result.append(name)
   
    print(result)
    return MainLayout(FilePage(result))
