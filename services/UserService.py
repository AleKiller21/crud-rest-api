from dao.UserDao import create_user, retrieve_user, get_users, update_user, delete_user


def add_user(payload):
    if __check_fields_existance(payload, 'first_name', 'last_name', 'email', 'gamertag'):
        __set_optional_fields(payload, 'address', 'profile_picture')
        return user_to_json(create_user(payload))
    else:
        return {'err': 'Missing fields in json'}


def get_user(gamertag):
    return user_to_json(retrieve_user(gamertag))


def get_all_users():
    result = get_users()
    return result


def modify_user(payload):
    if __check_fields_existance(payload, 'id', 'first_name', 'last_name', 'email', 'address', 'gamertag'):
        return update_user(payload)
    else:
        return {'err': 'Missing fields in json'}


def remove_user(payload):
    if __check_fields_existance(payload, 'id'):
        return delete_user(payload['id'])
    else:
        return {'err': 'Missing fields in json'}


def __check_fields_existance(payload, *fields):
    if all(key in payload for key in fields):
        return True


def __set_optional_fields(payload, *fields):
    for field in fields:
        if field not in payload.keys():
            payload[field] = ''


def user_to_json(user):
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'address': user.address,
        'gamertag': user.gamertag,
        'profile_picture': user.profile_picture
    }
