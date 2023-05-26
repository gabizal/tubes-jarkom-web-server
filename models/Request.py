class Request:
    def __init__(self, buffer: str) -> None:
        requestLine, data = buffer.split("\r\n", 1) # Membagi request line dan sisa data

        method, path, protocol = requestLine.split() # Membagi request line menjadi method, path, dan protocol

        self.method = method 
        self.path = path
        self.protocol = protocol

        headersRaw, bodyRaw = data.split("\r\n\r\n", 1) # Membagi headers dan body

        self.headers = self.parseHeaders(headersRaw) # menyimpan parse headers
        self.body = self.parseBody(bodyRaw) # menyimpan parse body

    def parseHeaders(self, headersRaw: str):
        """Membuat dictionary dari headers"""
        return dict(x.split(": ", 1) for x in headersRaw.split("\r\n"))

    def parseBody(self, body):
        """Membuat dictionary dari body"""
        return dict([x.split("=") for x in body.split("&")] if body else "")
