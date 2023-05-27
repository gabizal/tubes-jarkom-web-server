class Request:
    def __init__(self, buffer: str) -> None:
        """Membuat object request dari buffer"""

        # Split buffer to request line and data
        # Request line is the first line of the request
        # Data is the rest of the request
        requestLine, data = buffer.split("\r\n", 1)

        # Split request line to method, path, and protocol
        method, path, protocol = requestLine.split()

        # Set request object properties
        self.method = method
        self.path = path
        self.protocol = protocol

        # Split data to headers and body
        headersRaw, bodyRaw = data.split("\r\n\r\n", 1)

        # Set request object properties
        self.headers = self.parseHeaders(headersRaw)  # Parse headers
        self.body = self.parseBody(bodyRaw)  # Parse body

    def parseHeaders(self, headersRaw: str):
        """Membuat dictionary dari headers. Parse headers sebagai key dan value"""

        # Split headers to list of headers by "\r\n"
        # Then split each header to key and value by ": "
        return dict(x.split(": ", 1) for x in headersRaw.split("\r\n"))

    def parseBody(self, body):
        """Membuat dictionary dari body. Parse body sebagai key dan value"""

        # Split body to list of body by "&" (ampersand)
        # Then split each body to key and value by "=" (equal)
        return dict([x.split("=") for x in body.split("&")] if body else "")
