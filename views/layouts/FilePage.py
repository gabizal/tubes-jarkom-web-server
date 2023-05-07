from views.components.Footer import Footer
from views.components.Search import Search
from views.components.Title import Title
from views.components.List import List

def FilePage():
    return Title("Kessoku Database") + Search() + List() + Footer()