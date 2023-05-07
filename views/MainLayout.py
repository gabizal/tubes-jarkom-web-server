def MainLayout(content:str):
    template = open("views/index.html", "r").read()

    return template % content
