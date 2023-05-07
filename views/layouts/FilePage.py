import os
from views.components.Footer import Footer
from views.components.Search import Search
from views.components.FileTable import FileTable

def FilePage(files: list = []):
    
    if len(files) == 0:
        files = os.listdir('./database')

    search = Search()
    fileTable = FileTable(files)
    footer = Footer()

    page = search + fileTable + footer
    print("table", fileTable)
    print("FilePage", page)
    return page