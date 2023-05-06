class Request:
    def __init__(self, decodedRequest: str):
        print(decodedRequest)
        request = ''.join((line + '\n') for line in decodedRequest.splitlines())
        request_head, request_body = request.split('\n\n', 1)

        request_head = request_head.splitlines()
        request_headline = request_head[0]
        request_headers = dict(x.split(': ', 1) for x in request_head[1:])
        request_method, request_uri, request_proto = request_headline.split(' ', 3)

        self.method = request_method
        self.uri = request_uri
        self.proto = request_proto
        self.body = request_body
        self.headers = request_headers