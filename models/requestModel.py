# class Request:
#     def __init__(self, decodedRequest: str):
#         # print(decodedRequest)
#         request = ''.join((line + '\n') for line in decodedRequest.splitlines())
#         request_head, request_body = request.split('\n\n', 1)

#         request_head = request_head.splitlines()
#         request_headline = request_head[0]
#         request_headers = dict(x.split(': ', 1) for x in request_head[1:])
#         request_method, request_uri, request_proto = request_headline.split(' ', 3)

#         self.method = request_method
#         self.uri = request_uri
#         self.proto = request_proto
#         self.body = request_body
#         self.headers = request_headers


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

        print("headers:", self.headers)
        print("body:", self.body)

    def parseHeaders(self, headersRaw: str):
        return dict(x.split(": ", 1) for x in headersRaw[1:])

    def parseBody(self, body):
        return dict([x.split("=") for x in body.split("&")] if body else "")
