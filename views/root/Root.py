def Root(content: str):
    # template = open("views/root/html/index.html", "r").read()
    with open("views/root/html/index.html", "r") as templateFile:
        template = templateFile.read()

    return template % content
