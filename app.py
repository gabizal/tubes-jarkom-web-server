if __name__ == "__main__":
    from server import Server
    from handler import Handler

    server = Server("localhost", 80)
    server.addRoute("/", Handler.HomePage)
    server.addRoute("/search", Handler.SearchPage)
    server.run()
