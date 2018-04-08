from services.UtilService import check_fields_existance_in_payload
from services.MessageService import missing_fields_request
import services.AuthService as AuthService
from dao.UserDao import create_user, retrieve_user, get_users, update_user, delete_user, login_user
from beans.UserBean import User


def add_user(payload):
    if check_fields_existance_in_payload(payload, 'first_name', 'email', 'gamertag', 'password'):
        __set_optional_fields(payload, 'last_name', 'address', 'profile_picture', 'role')
        return __user_to_json(create_user(payload))
    else:
        return missing_fields_request


def get_user(gamertag):
    return __user_to_json(retrieve_user(gamertag))


def get_all_users():
    result = get_users()
    response = []
    for user in result:
        response.append(__user_to_json(user))

    return response


def modify_user(payload):
    if check_fields_existance_in_payload(payload, 'id', 'first_name', 'last_name', 'email', 'address', 'gamertag',
                                           'profile_picture'):
        return __user_to_json(update_user(payload))
    else:
        return missing_fields_request


def remove_user(payload):
    if check_fields_existance_in_payload(payload, 'id'):
        return __user_to_json(delete_user(payload['id']))
    else:
        return missing_fields_request


def login(payload):
    if not check_fields_existance_in_payload(payload, 'email', 'password'):
        return missing_fields_request

    result = login_user(payload)

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
