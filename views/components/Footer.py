def Footer():
    """Create footer that consist of author profile"""

    # Data
    dev_data = [
        {
            "username": "whoisgalih",
            "altf": "Profile Galih",
            "image": "https://avatars.githubusercontent.com/u/67363390?v=4",
        },
        {
            "username": "AbiyaMakruf",
            "altf": "Profile Abiya",
            "image": "https://avatars.githubusercontent.com/u/99990565?v=4",
        },
        {
            "username": "Rin4th",
            "altf": "Profile Rizal",
            "image": "https://avatars.githubusercontent.com/u/52568308?v=4",
        },
    ]

    # Open footer item file
    with open("views/components/html/footerItem.html", "r") as footerItemFile:
        footerItem = footerItemFile.read()

    # Create footer items
    footerItems = ""

    # Loop through dev data
    for user in dev_data:
        # Add footer item to footer items
        footerItems += footerItem % (
            user["username"],  # username
            user["image"],  # picture
            user["altf"],  # alt
            user["username"],  # username
        )

    # Open footer wrapper file
    with open("views/components/html/footerWrapper.html", "r") as footerWrapperFile:
        footers = footerWrapperFile.read()

    # Fill footer wrapper with footer items and return it
    return footers % footerItems
