from models.File import File


def FileTable(filesName: list):
    filesName.sort(key=str.casefold)

    with open("views/components/html/fileTableItem.html", "r") as fileTableItemHTML:
        fileTableItem = fileTableItemHTML.read()

    fileTableItems = ""

    for file in filesName:
        file = File(file)

        fileTableItems += fileTableItem % (
            file.name,  # name
            file.icon,  # icon
            file.name,  # name
            file.size,  # size
        )

    if fileTableItems == "":
        with open("views/components/html/fileNotFound.html", "r") as filesNotFoundHTML:
            fileTableItems = filesNotFoundHTML.read()

    with open("views/components/html/fileTable.html", "r") as fileTable:
        table = fileTable.read()

    table = table % fileTableItems

    return table
