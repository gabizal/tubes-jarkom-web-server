import os


class File:
    def __init__(self, name: str):
        self.name = name # set file name
        self.size = self.humanReadableSize() # set file size using humanReadableSize()
        self.icon = self.getIcon() # set file icon using getIcon()

    def humanReadableSize(self):
        fileSize = os.path.getsize(f"database/{self.name}") # get file size

        """Mengubah file size menjadi human readable format"""
        for unit in ["bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]:
            if abs(fileSize) < 1024.0: # Mengecek apakah file size lebih kecil dari 1024
                return f"{fileSize:3.1f}{unit}" # Mengembalikan file size dengan format 3.1f (3 angka di depan, 1 angka di belakang koma) dan unit
            fileSize /= 1024.0 # Mengubah file size menjadi satuan yang lebih besar

        return f"{fileSize:.1f}YB" # Mengembalikan file size dengan format dengan tipe YB

    def getIcon(self):
        fileExtension = self.name.split(".")[-1]  # Mendapatkan file extension

        # file icons list
        fileIconsList = {
            # icon: [extensions]
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

        # Mengecek apakah file extension ada di fileIconsList
        for icon, exntensions in fileIconsList.items():
            if fileExtension in exntensions:
                return icon

        # Mengembalikan file icon default
        return "file"
