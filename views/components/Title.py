def Title(title):
    """Creates a big title for the page"""

    # Open title file
    with open("views/components/html/title.html", "r") as titleFile:
        titlePage = titleFile.read()

    # Fill title file with title and return it
    return titlePage % title
