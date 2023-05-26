def Title(title):
    with open("views/components/html/title.html", "r") as titleFile:
        titlePage = titleFile.read()

    return titlePage % title
