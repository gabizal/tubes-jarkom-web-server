from views.root import Root
from views.components import Footer, Title, Search


def HomePage():
    home: str = Title("Kessoku <br/> Database") + Search() + Footer()
    return Root(home)
