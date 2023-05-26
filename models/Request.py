class Request:
    def __init__(self, buffer: str) -> None:
        request, data = buffer.split("\r\n", 1)

        method, path, protocol = request.split()

        self.method = method
        self.path = path
        self.protocol = protocol

        headersRaw, bodyRaw = data.split("\r\n\r\n", 1)

        self.headers = self.parseHeaders(headersRaw)
        self.body = self.parseBody(bodyRaw)

    def parseHeaders(self, headersRaw: str):
        return dict(x.split(": ", 1) for x in headersRaw.split("\r\n"))

    def parseBody(self, body):
        return dict([x.split("=") for x in body.split("&")] if body else "")
