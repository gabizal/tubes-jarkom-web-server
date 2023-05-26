from views.root import Root
from views.components import Footer, Title, Search, FileTable


def FilePage(search: str = "", files: list = []):
    title = Title("Kessoku <br/> Database")
    search = Search(search)
    fileTable = FileTable(files)
    footer = Footer()

    page = title + search + fileTable + footer
    return Root(page)
