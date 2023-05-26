def Search(value: str = ""):
    with open("views/components/html/search.html", "r") as search_html_file:
        search_html = search_html_file.read()

    search_html = search_html % (value)

    return search_html
