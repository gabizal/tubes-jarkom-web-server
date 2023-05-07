def Search(value: str = ""):
    search_html_file = open("views/components/html/search.html", "r")
    search_html = search_html_file.read()
    search_html_file.close()

    search_html = search_html % (value)
    
    return search_html