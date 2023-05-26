if __name__ == "__main__":
    from server import Server
    from handler import Handler

    """Membuat server dan menambahkan route ke server"""
    server = Server("localhost", 80)
    server.addRoute("/", Handler.HomePage) # Menambahkan route ke server
    server.addRoute("/search", Handler.SearchPage) # Menambahkan route ke server untuk pencarian file
    server.run() # Menjalankan server
