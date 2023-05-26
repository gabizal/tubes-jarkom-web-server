from views.root.Root import Root
from views.components.Footer import Footer
from views.components.Title import Title


def ErrorPage(code: int = 404, message: str = "Not Found"):
    message = message.split(" ")
    title = Title(f"404 {message[0]} <br/> {message[1]}")
    footer = Footer()

    return Root(title + footer)
