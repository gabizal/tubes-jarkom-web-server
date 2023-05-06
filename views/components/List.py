def List(list_data):
    
    list_html = """
    <div class="flex flex-col items-center">
        <div class="flex flex-row">
            <div class="basis-3/5" style="font-family: 'Poppins', sans-serif;">Name</div>
            <div class="basis-2/5" style="font-family: 'Poppins', sans-serif;">Size</div>
        </div>
        %s
    </div>
    """

    list_file = """
    <a class="flex flex-row rounded-lg" style="background-color: #984ED8;" href="database/%s" target="blank">
        <div class="basis-3/5">
            <div class="flex flex-row">
                <i class="fa fa-solid fa-file-%s fa-xl" style="color: #bdbfc1;"></i>
                <div class="text-white" style="font-family: 'Poppins', sans-serif;">%s</div>
            </div>
        </div>
        <div class="basis-2/5" style="font-family: 'Poppins', sans-serif;">%s</div>
    </a>
    """
