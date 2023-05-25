class Server:
    def __init__(self, host, port, status):
        self.name = f"{host}:{port}"
        self.host = host
        self.port = port

    def __repr__(self):
        return "<Server %r>" % self.name
