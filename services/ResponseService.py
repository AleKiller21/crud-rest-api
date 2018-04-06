from flask import Response


def set_headers(value, headers):
    """Returns a response with the value and headers sent as arguments"""

    resp = Response(value)
    for head in headers:
        resp.headers[head] = headers[head]

    return resp
