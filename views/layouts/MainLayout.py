from views.components.Footer import Footer
from views.components.Search import Search
from views.components.Title import Title


def MainLayout(content:str):
    html_body = open("views/index.html", "r").read()

    return html_body % content
