import base64


def to_base64(email, password):
    token = '%s:%s' % (email, password)
    return base64.b64encode(token.encode('utf-8'))


def check_token_existance(headers):
    return 'Authorization' in headers.keys()


def extract_token_from_header(header):
    return header[header.find(' ') + 1:]


def get_user_email_from_token(headers):
    if not check_token_existance(headers):
        raise Exception('You must login')

    token = extract_token_from_header(headers['Authorization'])
    return __authenticate(token)


def __authenticate(token):
    result = base64.b64decode(token).decode('utf-8')
    index = result.find(':')

    if not index:
        raise Exception('session has expired. Please login again')

    email = result[:index]
    password = result[index + 1:]

    return {'email': email, 'password': password}
