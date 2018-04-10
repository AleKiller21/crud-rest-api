
missing_fields_request = {'message': 'Missing fields in request', 'code': 400}

authentication_failed = {'message': 'You must log in', 'code': 401}

lack_of_privilege = {'message': 'You do not have the privileges to carry on this action', 'code': 403}

user_info_duplication = {'message': 'Either the email or gamertag already exist in our database', 'code': 400}


def generate_success_message(message, data):
    return {'message': message, 'data': data, 'code': 200}


def generate_internal_server_error(message):
    return {'message': message, 'code': 500}


def generate_custom_message(message, code, data):
    return {'message': message, 'data': data, 'code': code}
