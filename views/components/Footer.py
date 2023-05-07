def Footer():
    
    dev_data = {
        "github": ["whoisgalih", "AbiyaMakruf", "Rin4th"],
        "altf": ["Profile Galih", "Profile Abiya", "Profile Rizal"],
        "profile": ["https://avatars.githubusercontent.com/u/67363390?v=4", "https://avatars.githubusercontent.com/u/99990565?v=4", "https://avatars.githubusercontent.com/u/52568308?v=4"]
    }

    # convert that to user based dictionary
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
    
    user_html = """
    <a href="https://github.com/%s" target="blank">
        <div style="background-color: #984ED8;" class="flex flex-row py-8 pl-10 pr-16">
            <img src="%s" alt="%s" class="rounded-full border-none h-28">
            <div style="font-family: 'Poppins', sans-serif;" class="text-[20px]">
                %s
            </div>
        </div>
    </a>
    """

    user_list = ""

    for user in dev_data:
        user_list += user_html % (user["github"], user["profile"], user["altf"], user["github"])


    
    
    html_footer = """
    <div class="flex flex-row">
        %s
    </div>
    """

    return html_footer % user_list

