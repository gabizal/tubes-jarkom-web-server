from views.root import Root
from views.components import Footer, Title


def ErrorPage(code: int = 404, message: str = "Not Found"):
    """Create error page"""

    # Split message by space
    message = message.split(" ")

    # Create title and footer
    title = Title(f"404 {message[0]} <br/> {message[1]}")
    footer = Footer()

    # Return error page using root component
    return Root(title + footer)
