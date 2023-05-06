from views.components.Footer import Footer
from views.components.Search import Search
from views.components.Title import Title


def HomePage():
    html_body = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script src="https://cdn.tailwindcss.com"></script>
            <link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">
            <title>Local Server</title>
            <style>
                @font-face { font-family: Thunder; src: url('../assets/Thunder-BlackLC.ttf'); } 
                @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
                input[type="text"],
                    textarea {
                        border: none;
                        outline: none;
                    }
            </style>
        </head>
        <body style="background-color: #984ED8">
            <div class="flex flex-col items-center ">
                {} <!-- Title --!>
                {} <!-- Search --!>
                {} <!-- Footer --!>
            </div>
        </body>
        </html>
    """

    return html_body.format(Title(), Search(), Footer())
