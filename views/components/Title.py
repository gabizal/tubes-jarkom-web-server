def Title(title):
    # titleFile = open("views/components/html/title.html", "r")
    # titlePage = titleFile.read()
    # titleFile.close()

    with open("views/components/html/title.html", "r") as titleFile:
        titlePage = titleFile.read()

    return titlePage % title
