import jwt
import datetime
from dao.UserDao import get_user_role
import services.MessageService as MessageService

key = 'SanServices01$'


def generate_token(payload):
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=20)
    return jwt.encode(payload, key, algorithm='HS256').decode('utf-8')


def check_token_existance(headers):
    return 'Authorization' in headers.keys()


def extract_token_from_header(header):
    return header[header.find(' ') + 1:]


def authenticate(endpoint, headers):
    reestricted_endpoints = ['get_user', 'get_users', 'update_user', 'delete_user', 'add_game', 'update_game',
                             'delete_game', 'add_order', 'get_order_by_order_number', 'get_order_by_game_id',
                             'get_order_by_user', 'get_orders', 'update_order']

    admin_endpoints = ['get_users', 'delete_user', 'add_game', 'update_game', 'delete_game',
                       'get_order_by_order_number', 'get_order_by_game_id', 'get_orders', 'update_order']

    if endpoint not in reestricted_endpoints:
        return MessageService.generate_success_message('', {})

    try:
        token = extract_token_from_header(headers['Authorization'])
        data = decode_token(token)

        if endpoint in admin_endpoints:
            is_admin = __is_user_admin(data['id'])
            if not is_admin:
                return MessageService.lack_of_privilege

    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError):
        return MessageService.authentication_required

    except Exception:
        return MessageService.generate_internal_server_error('An error has ocurred')

    return MessageService.generate_success_message('', {})


def decode_token(token):
    result = extract_token_from_header(token)
    return jwt.decode(result, key, algorithms=['HS256'])


def __is_user_admin(id):
    result = get_user_role(id)

    if result:
        return result['role'] == 'admin'
    else:
        return None
