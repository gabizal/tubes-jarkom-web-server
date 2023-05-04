import os
from messageHandler import *

def handlePOST(request):
    search = request.split("\n")[25].replace("\r", "")
    result = []
    files = os.listdir('./database')
    for name in files:
        if search in name:
            result.append(name)

    return htmlRenderer(search, result)