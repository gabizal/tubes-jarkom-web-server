class Request:
    def __init__(self, decodedRequest: str):
        # print(decodedRequest)
        request = ''.join((line + '\n') for line in decodedRequest.splitlines())
        requestHead, requestBody = request.split('\n\n', 1)

        requestHead = requestHead.splitlines()
        requestHeadline = requestHead[0]
        requestHeaders = dict(x.split(': ', 1) for x in requestHead[1:])
        requestMethod, requestUri, requestProto = requestHeadline.split(' ', 3)

        self.method = requestMethod
        self.uri = requestUri
        self.proto = requestProto
        self.body = requestBody
        self.headers = requestHeaders