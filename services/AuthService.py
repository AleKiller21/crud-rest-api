import base64


def to_base64(email, password):
    token = '%s:%s' % (email, password)
    return base64.b64encode(token.encode('utf-8'))


def authenticate(token):
    try:
        result = base64.b64decode(token).decode('utf-8')
        index = result.find(':')

        if not index:
            raise Exception('authentication failed')

        email = result[:index]
        password = result[index + 1:]
        return {'email': email, 'password': password}

    except Exception as e:
        print(e)
        return {'err': e}
