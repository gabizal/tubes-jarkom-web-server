import os
from handler.messageHandler import *

def handlePOST(request_body: str):
    search = request_body.split("\n")[3].replace("\r", "")
    result = []
    files = os.listdir('./database')
    for name in files:
        if search.lower() in name.lower():
            result.append(name)
   

    return htmlRenderer(search, result)
