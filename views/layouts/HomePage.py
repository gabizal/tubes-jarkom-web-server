from views.root.Root import Root
from views.components.Footer import Footer
from views.components.Search import Search
from views.components.Title import Title


def HomePage():
    home: str = Title("Kessoku <br/> Database") + Search() + Footer()
    return Root(home)
