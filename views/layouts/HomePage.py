from views.root import Root
from views.components import Footer, Title, Search


def HomePage():
    """Create home page"""

    # Create title, search, and footer
    home: str = Title("Kessoku <br/> Database") + Search() + Footer()

    # Return home page using root component
    return Root(home)
