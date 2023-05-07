from views.components.Footer import Footer
from views.components.Title import Title


def page404():
    title = Title("404 Not <br/> Found")
    footer = Footer()

    return title + footer
