def Search():
    search_html = """
    <div class="flex flex-row rounded-lg p-6" style="background-color: #984ED8;">
        <form action="/" method="POST" class="">
            <input type="text" name="search" placeholder="Cari file disini" enctype="multipart/form-data">
            <button type="submit" disabled>
                <i class="fa fa-solid fa-search fa-xl" style="color: #bdbfc1;"></i>
            </button>
        </form>
    </div>
    """
    
    return search_html