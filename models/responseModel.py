import mimetypes

from views.layouts.page404 import page404


class Response:
    def __init__(self, status: int, data: bytes, headers: dict = None):
        self.status: int = status
        self.data: bytes = data
        self.headers: dict = headers or {}

    def __str__(self):
        return (
            f"HTTP/1.1 {self.status} {self.statusText(self.status)}\r\n"
            + "".join([f"{key}: {value}\r\n" for key, value in self.headers.items()])
            + "\r\n"
            + self.data.decode()
        )

    def __bytes__(self):
        statusLine = f"HTTP/1.1 {self.status} {self.statusText(self.status)}\r\n"
        headerLines = "".join(
            [f"{key}: {value}\r\n" for key, value in self.headers.items()]
        )
        return statusLine.encode() + headerLines.encode() + b"\r\n" + self.data

    def statusText(self, status: int) -> str:
        if status == 200:
            return "OK"
        elif status == 404:
            return "Not Found"
        else:
            return "Unknown"

    @staticmethod
    def defineContentType(path):
        return mimetypes.guess_type(path)[0] or "text/plain"

    @staticmethod
    def fromFile(path: str):
        try:
            print(path)
            with open(path, "rb") as f:
                data = f.read()

            contentType: str = Response.defineContentType(path)
            return Response(
                200, data, {"Content-Type": contentType, "Content-Length": len(data)}
            )
        except FileNotFoundError:
            return Response.errorResponse()

    @staticmethod
    def fromText(text: str) -> bytes:
        return Response(200, text.encode(), {"Content-Type": "text/html"})

    @staticmethod
    def errorResponse() -> bytes:
        return Response(404, page404().encode(), {"Content-Type": "text/html"})
