from models.File import File


def FileTable(filesName: list):
    """Create file table from files name"""

    # Sort files name by case insensitive
    filesName.sort(key=str.casefold)

    # Read fileTableItem.html
    with open("views/components/html/fileTableItem.html", "r") as fileTableItemHTML:
        fileTableItem = fileTableItemHTML.read()

    # Create file table items
    fileTableItems = ""

    # Loop through files name
    for file in filesName:
        # Create file object to get file icon and file size in human readable
        file = File(file)

        # Add file table item to file table items
        fileTableItems += fileTableItem % (
            file.name,  # name
            file.icon,  # icon
            file.name,  # name
            file.size,  # size
        )

    # If file table items is empty
    if fileTableItems == "":
        # Display file not found
        # Read fileNotFound.html
        with open("views/components/html/fileNotFound.html", "r") as filesNotFoundHTML:
            fileTableItems = filesNotFoundHTML.read()

    # Read fileTable.html
    with open("views/components/html/fileTable.html", "r") as fileTable:
        table = fileTable.read()

    # Fill file table with file table items
    table = table % fileTableItems

    # Return file table
    return table
