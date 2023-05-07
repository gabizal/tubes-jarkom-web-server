from views.components.Footer import Footer
from views.components.FileTable import FileTable
from views.components.Search import Search

def HomePage():
    return Search() + Footer()