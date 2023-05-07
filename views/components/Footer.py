def Footer():
    dev_data = [
        {
            "github": "whoisgalih",
            "altf": "Profile Galih",
            "profile": "https://avatars.githubusercontent.com/u/67363390?v=4"
        },
        {
            "github": "AbiyaMakruf",
            "altf": "Profile Abiya",
            "profile": "https://avatars.githubusercontent.com/u/99990565?v=4"
        },
        {
            "github": "Rin4th",
            "altf": "Profile Rizal",
            "profile": "https://avatars.githubusercontent.com/u/52568308?v=4"
        }
    ]

    footerItem = open("views/components/html/footerItem.html", "r").read()
    footerItems = ""

    for user in dev_data:
        footerItems += footerItem % (user["profile"], user["altf"], user["github"])
    
    footers = open("views/components/html/footerWrapper.html", "r").read()

    return footers % footerItems