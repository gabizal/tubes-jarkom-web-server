import os

def FileTable(filesName: list): 
    extensions = {
        "pdf": ["pdf"],
        "txt": ["txt"],
        "mp3": ["mp3"],
        "mp4": ["mp4"],
        "image": ["jpg", "png", "jpeg","webp"],
        "document": ["docx", "pptx", "xlsx", "doc", "ppt", "xls"],
        "archive": ["zip", "rar"],
        "code": ["html", "css", "js", "py"]
    }

    database_file = {k: [name for name in filesName if name.split(".")[-1] in v] for k, v in extensions.items()}

    database_icon ={
        "pdf": "pdf",
        "txt": "lines",
        "mp3": "audio",
        "mp4": "video",
        "image": "image",
        "document": "word",
        "archive": "archive",
    }
    
    fileTableItem = open("views/components/html/fileTableItem.html", "r").read()
    fileTableItems = ""

    for fileType, files in database_file.items():
        for file in files:
            try:
                icon = "file-" + database_icon[fileType]
            except KeyError:
                icon = "file"
            # name, icon, name, size
            fileTableItems += fileTableItem % (file, icon, file, os.path.getsize("database/"+file))
    
    fileTable = open("views/components/html/fileTable.html", "r")
    table = fileTable.read()
    fileTable.close()

    table = table % fileTableItems

    return table