import os

def List(list_data):
    extensions = {
        "pdf": ["pdf"],
        "txt": ["txt"],
        "mp3": ["mp3"],
        "mp4": ["mp4"],
        "image": ["jpg", "png", "jpeg"],
        "document": ["docx", "pptx", "xlsx", "doc", "ppt", "xls"],
        "archive": ["zip", "rar"],
        "code": ["html", "css", "js", "py"]
    }

    database_file = {k: [name for name in data if name.split(".")[-1] in v] for k, v in extensions.items()}
    print(database_file)
    database_icon ={
        "pdf": "pdf",
        "txt": "lines",
        "mp3": "audio",
        "mp4": "video",
        "image": "image",
        "document": "word",
        "archive": "archive",
    }
    
    list_html = """
    <div class="flex flex-col items-center">
        <div class="flex flex-row">
            <div class="basis-3/5" style="font-family: 'Poppins', sans-serif;">Name</div>
            <div class="basis-2/5" style="font-family: 'Poppins', sans-serif;">Size</div>
        </div>
        %s
    </div>
    """

    list_file = """
    <a class="flex flex-row rounded-lg" style="background-color: #984ED8;" href="database/%s" target="blank">
        <div class="basis-3/5">
            <div class="flex flex-row">
                <i class="fa fa-solid fa-file-%s fa-xl" style="color: #bdbfc1;"></i>
                <div class="text-white" style="font-family: 'Poppins', sans-serif;">%s</div>
            </div>
        </div>
        <div class="basis-2/5" style="font-family: 'Poppins', sans-serif;">%s</div>
    </a>
    """

    for key in database_file:
        if len(database_file[key]) > 0:
            for value in database_file[key]:
                list_html += list_file % (value, database_icon[key], value, os.path.getsize("database/"+value))

    return list_html % list_data