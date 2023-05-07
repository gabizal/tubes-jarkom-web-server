def Title(title):
    titleFile = open("views/components/html/title.html", "r")
    titlePage = titleFile.read()
    titleFile.close()
    
    return titlePage % title