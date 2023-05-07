import os
from views.components.Footer import Footer
from views.components.Search import Search
from views.components.FileTable import FileTable
from views.components.Title import Title

def FilePage(search: str = "", files: list = []):
    title = Title("Kessoku <br/> Database")
    search = Search(search)
    fileTable = FileTable(files)
    footer = Footer()

    page = title + search + fileTable + footer
    return page