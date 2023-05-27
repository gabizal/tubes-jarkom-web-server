def Root(content: str):
    """Create root page. Root page is used to wrap all pages with style and script"""

    # Read index.html
    with open("views/root/html/index.html", "r") as templateFile:
        template = templateFile.read()

    # Fill index.html with content and return it
    return template % content
