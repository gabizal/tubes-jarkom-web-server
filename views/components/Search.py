def Search(value: str = ""):
    """Create search component if there is an input before, then display it"""

    # Read search.html
    with open("views/components/html/search.html", "r") as search_html_file:
        search_html = search_html_file.read()

    # If there is a value
    # Then fill search component with value
    search_html = search_html % (value)

    # Return search component
    return search_html
