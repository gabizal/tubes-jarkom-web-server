def Footer():
    
    dev_data = {
        "github": ["whoisgalih", "AbiyaMakruf", "Rin4th"],
        "altf": ["Profile Galih", "Profile Abiya", "Profile Rizal"],
        "profile": ["https://avatars.githubusercontent.com/u/67363390?v=4", "https://avatars.githubusercontent.com/u/99990565?v=4", "https://avatars.githubusercontent.com/u/52568308?v=4"]
    }
    
    user_html = """
    <a hres="https://github.com/%s" target="blank">
        <div style="background-color: #D9D9DD9;" class="flex flex-row py-8 pl-10 pr-16">
            <img src="" alt="%s" class="rounded-full border-none">
            <div style="font-family: 'Poppins', sans-serif;" class="text-[20px]">
                %s
            </div>
        </div>
    </a>
    """

    user_list = ""

    for _, value in dev_data:
        for key in dev_data:
            user_list += user_html % (dev_data[key][value], dev_data[key][value], dev_data[key][value])

    
    
    html_footer = """
    <div class="flex flex-row">
        %s
    </div>
    """

    return html_footer % user_list

