from services.UtilService import check_fields_existance_in_payload
import services.MessageService as MessageService
import services.AuthService as AuthService
import dao.UserDao as UserDao
from beans.UserBean import User


def add_user(payload):
    if check_fields_existance_in_payload(payload, 'first_name', 'email', 'gamertag', 'password'):
        __set_optional_fields(payload, 'last_name', 'address', 'profile_picture', 'role')
        return __user_to_json(UserDao.create_user(payload))
    else:
        return MessageService.missing_fields_request


def get_user(gamertag, headers):
    auth = AuthService.get_user_email_from_token(headers)

    if 'err' in auth.keys():
        return auth

    result = UserDao.get_user_role_gamertag(auth['email'])

    if result['role'] == 'admin':
        return __user_to_json(UserDao.retrieve_user(gamertag))
    else:
        return __user_to_json(UserDao.retrieve_user(result['gamertag']))


def get_all_users(headers):
    auth = AuthService.get_user_email_from_token(headers)

    if 'err' in auth.keys():
        return auth

    if not __is_user_admin(auth):
        return MessageService.lack_of_privilege

    result = UserDao.get_users()
    response = []
    for user in result:
        response.append(__user_to_json(user))

    return response


def modify_user(payload):
    if check_fields_existance_in_payload(payload, 'id', 'first_name', 'last_name', 'email', 'address', 'gamertag',
                                         'profile_picture'):
        return __user_to_json(UserDao.update_user(payload))
    else:
        return MessageService.missing_fields_request


def remove_user(payload, headers):
    auth = AuthService.get_user_email_from_token(headers)

    if 'err' in auth.keys():
        return auth

    if not __is_user_admin(auth):
        return MessageService.lack_of_privilege

    if check_fields_existance_in_payload(payload, 'id'):
        return __user_to_json(UserDao.delete_user(payload['id']))
    else:
        return MessageService.missing_fields_request


def login(payload):
    if not check_fields_existance_in_payload(payload, 'email', 'password'):
        return MessageService.missing_fields_request

    result = UserDao.login_user(payload)

    if 'err' in result.keys():
        return result

    return {
        'token': 'Basic ' + AuthService.to_base64(payload['email'], payload['password']).decode('utf-8'),
        'gamertag': result['gamertag']
    }


def __set_optional_fields(payload, *fields):
    for field in fields:
        if field not in payload.keys():
            if field == 'role':
                payload[field] = 'customer'
            else:
                payload[field] = ''


def __user_to_json(user):
    if type(user) is User:
        return user.to_dictionary()
    else:
        return user


def __is_user_admin(auth):
    result = UserDao.get_user_role_gamertag(auth['email'])
    return result['role'] == 'admin'
