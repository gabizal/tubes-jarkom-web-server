import os


class File:
    def __init__(self, name: str):
        self.name = name
        self.size = self.humanReadableSize()
        self.icon = self.getIcon()

    def humanReadableSize(self):
        fileSize = os.path.getsize(f"database/{self.name}")
        for unit in ["bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]:
            if abs(fileSize) < 1024.0:
                return f"{fileSize:3.1f}{unit}"
            fileSize /= 1024.0
        return f"{fileSize:.1f}YB"

    def getIcon(self):
        # get file extension
        fileExtension = self.name.split(".")[-1]

        # file icons list
        fileIconsList = {
            "file-pdf": ["pdf"],
            "file-lines": ["txt"],
            "file-audio": ["mp3", "ogg", "wav"],
            "file-video": ["mp4"],
            "file-image": ["jpg", "png", "jpeg"],
            "file-word": ["docx", "doc"],
            "file-excel": ["xlsx", "xls"],
            "file-powerpoint": ["pptx", "ppt"],
            "file-csv": ["csv"],
            "file-archive": ["zip", "rar"],
            "file-code": [
                "html",
                "css",
                "js",
                "py",
                "go",
                "c",
                "cpp",
                "java",
                "php",
            ],
        }

        # check if file extension is in fileIconsList
        for icon, exntensions in fileIconsList.items():
            if fileExtension in exntensions:
                return icon

        # return default file icon
        return "file"
