
missing_fields_request = {'message': 'There was an error with the request sent to the server', 'code': 400}

authentication_required = {'message': 'Authentication is required to continue', 'code': 401}

authentication_failed = {'message': 'Either email or password is wrong', 'code': 401}

lack_of_privilege = {'message': 'You do not have the privileges to carry on this action', 'code': 403}

user_info_duplication = {'message': 'Either the email or gamertag already exist in our database', 'code': 400}


def generate_success_message(message, data):
    return {'message': message, 'data': data, 'code': 200}


def generate_internal_server_error(exception):
    return {'message': str(exception), 'code': 500}
