def Root(content: str):
    with open("views/root/html/index.html", "r") as templateFile:
        template = templateFile.read()

    return template % content
