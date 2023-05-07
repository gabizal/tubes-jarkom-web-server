from views.components.Footer import Footer
from views.components.Search import Search
from views.components.Title import Title


def HomePage():
    return Title("Kessoku <br/> Database") + Search() + Footer()