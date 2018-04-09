import base64
import services.MessageService as MessageService


def to_base64(email, password):
    token = '%s:%s' % (email, password)
    return base64.b64encode(token.encode('utf-8'))


def check_token_existance(headers):
    return 'Authorization' in headers.keys()


def extract_token_from_header(header):
    return header[header.find(' ') + 1:]


def get_user_email_from_token(headers):
    if not check_token_existance(headers):
        return MessageService.authentication_failed

    token = extract_token_from_header(headers['Authorization'])
    auth = __authenticate(token)

    if 'err' in auth.keys():
        return {'err': 'session has expired. Please login again'}

    return auth


def __authenticate(token):
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
