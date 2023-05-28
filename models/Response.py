import mimetypes

from views import ErrorPage


class Response:
    def __init__(self, status: int, data: bytes, headers: dict = None):
        """Initialize response"""

        # Set response object properties
        self.status: int = status  # Response status code
        self.data: bytes = data  # Response body in bytes
        self.headers: dict = headers or {}  # Response headers

    def __str__(self):
        """Mengembalikan response sebagai string. Digunakan untuk debugging"""

        # Return response sebagai string
        return (
            f"HTTP/1.1 {self.status} {self.statusText(self.status)}\r\n"  # Status line
            + "".join(
                [f"{key}: {value}\r\n" for key, value in self.headers.items()]
            )  # Headers
            + "\r\n"  # Newline diantara headers dan body
            + self.data.decode()  # Body
        )

    def __bytes__(self):
        """Mengembalikan response sebagai bytes. Digunakan untuk mengirim response ke client"""
        statusLine = (
            f"HTTP/1.1 {self.status} {self.statusText(self.status)}\r\n"  # Status line
        )
        headerLines = "".join(
            [f"{key}: {value}\r\n" for key, value in self.headers.items()]
        )  # Headers
        return (
            statusLine.encode() + headerLines.encode() + b"\r\n" + self.data
        )  # Response

    def statusText(self, status: int) -> str:
        """Mengembalikan status code sebagai teks"""
        if status == 200:
            return "OK"
        elif status == 404:
            return "Not Found"
        else:
            return "Unknown"

    # Using static method because it doesn't need to create instance
    @staticmethod
    def defineContentType(path) -> str:
        """Mengembalikan content type dari path"""
        return mimetypes.guess_type(path)[0] or "text/plain"  # Return content type

    @staticmethod
    def fromFile(path: str) -> bytes:
        """Mengembalikan response dari file"""

        # Mencoba membuka file
        try:
            with open(path, "rb") as f:
                data = f.read()  # Read file

            # Menentukan content type dari path
            contentType: str = Response.defineContentType(path)

            # Mengembalikan response sebagai bytes
            return bytes(
                Response(
                    200,  # Status code
                    data,  # Data dari file dalam bytes
                    {
                        "Content-Type": contentType,
                        "Content-Length": len(data),
                    },  # Headers
                )
            )
        # Jika file tidak ditemukan
        except FileNotFoundError:
            return Response.errorResponse()  # Mengembalikan error response

    @staticmethod
    def fromText(text: str) -> bytes:
        """Return response from text"""

        # Return response as bytes
        return bytes(
            Response(
                200,  # Status code
                text.encode(),  # Text in bytes
                {"Content-Type": "text/html"},  # Headers, define it as html
            )
        )

    @staticmethod
    def errorResponse() -> bytes:
        """Return error response"""

        # Return response as bytes
        return bytes(
            Response(
                404,  # Status code
                ErrorPage().encode(),  # Error page in bytes
                {"Content-Type": "text/html"},  # Headers, define it as html
            )
        )
