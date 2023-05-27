from views.root import Root
from views.components import Footer, Title, Search, FileTable


def FilePage(search: str = "", files: list = []):
    """Create file page"""

    # Create title, search, file table, and footer
    title = Title("Kessoku <br/> Database")
    search = Search(search)
    fileTable = FileTable(files)
    footer = Footer()

    # Return file page using root component
    page = title + search + fileTable + footer
    return Root(page)
