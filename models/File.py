import os


class File:
    def __init__(self, name: str):
        # set file name
        self.name = name
        # set file size using human readable size
        self.size = self.humanReadableSize()
        # set file icon using getIcon()
        self.icon = self.getIcon()

    def humanReadableSize(self):
        # get file size
        fileSize = os.path.getsize(f"database/{self.name}")

        # convert file size to human readable
        for unit in ["bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]:
            # check if file size is less than 1024
            if abs(fileSize) < 1024.0:
                # return file size with unit
                return f"{fileSize:3.1f}{unit}"
            # if file size is more than 1024, then divide file size by 1024
            fileSize /= 1024.0

        # return YB if file size is bigger than ZB
        return f"{fileSize:.1f}YB"

    def getIcon(self):
        # get file extension
        fileExtension = self.name.split(".")[-1]

        # file icons list
        fileIconsList = {
            # icon: [extensions]
            # extensions must be lowercase
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
