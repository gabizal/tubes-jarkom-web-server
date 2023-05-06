import os
from handler.messageHandler import *

def handlePOST(request_body: str):
    search = request_body.split("\n")[2].replace("\r", "")
    result = []
    files = os.listdir('./database')
    for name in files:
        if search in name:
            result.append(name)
   

    return htmlRenderer(search, result)
