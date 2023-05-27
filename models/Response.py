import mimetypes

from views import ErrorPage


class Response:
    def __init__(self, status: int, data: bytes, headers: dict = None):
        """Initialize response"""

        # Set response object properties
        self.status: int = status
        self.data: bytes = data
        self.headers: dict = headers or {}

    def __str__(self):
        """Return response as string. Used for debugging"""

        # Return response as string
        return (
            f"HTTP/1.1 {self.status} {self.statusText(self.status)}\r\n"  # Status line
            + "".join(
                [f"{key}: {value}\r\n" for key, value in self.headers.items()]
            )  # Headers
            + "\r\n"  # Newline between headers and body
            + self.data.decode()  # Body
        )

    def __bytes__(self):
        """Return response as bytes. Used to send response to client"""
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
        """Return status text from status code"""
        if status == 200:
            return "OK"
        elif status == 404:
            return "Not Found"
        else:
            return "Unknown"

    # Using static method because it doesn't need to create instance
    @staticmethod
    def defineContentType(path) -> str:
        """Return content type from path"""
        return mimetypes.guess_type(path)[0] or "text/plain"  # Return content type

    @staticmethod
    def fromFile(path: str) -> bytes:
        """Return response from file"""

        # Try to open file
        try:
            # Open file, read file, and close file
            with open(path, "rb") as f:
                data = f.read()  # Read file

            # Define content type from path
            contentType: str = Response.defineContentType(path)

            # Return response as bytes
            return bytes(
                Response(
                    200,  # Status code
                    data,  # Data from file in bytes
                    {
                        "Content-Type": contentType,
                        "Content-Length": len(data),
                    },  # Headers
                )
            )
        # If file not found
        except FileNotFoundError:
            return Response.errorResponse()  # Return error response

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
