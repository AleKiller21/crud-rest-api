from dao.UserDao import create_user, retrieve_user, get_users, update_user, delete_user
from beans.UserBean import User


def add_user(payload):
    if __check_fields_existance(payload, 'first_name', 'last_name', 'email', 'gamertag'):
        __set_optional_fields(payload, 'address', 'profile_picture')
        return __user_to_json(create_user(payload))
    else:
        return {'err': 'Missing fields in json'}


def get_user(gamertag):
    return __user_to_json(retrieve_user(gamertag))


def get_all_users():
    result = get_users()
    response = []
    for user in result:
        response.append(__user_to_json(user))

    return response


def modify_user(payload):
    if __check_fields_existance(payload, 'id', 'first_name', 'last_name', 'email', 'address', 'gamertag',
                                'profile_picture'):
        return __user_to_json(update_user(payload))
    else:
        return {'err': 'Missing fields in json'}


def remove_user(payload):
    if __check_fields_existance(payload, 'id'):
        return __user_to_json(delete_user(payload['id']))
    else:
        return {'err': 'Missing fields in json'}


def __check_fields_existance(payload, *fields):
    if all(key in payload for key in fields):
        return True


def __set_optional_fields(payload, *fields):
    for field in fields:
        if field not in payload.keys():
            payload[field] = ''


def __user_to_json(user):
    if type(user) is User:
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'address': user.address,
            'gamertag': user.gamertag,
            'profile_picture': user.profile_picture
        }
    else:
        return user
