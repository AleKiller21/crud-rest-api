from services.DbService import DbService
from beans.UserBean import User


def create_user(payload):
    query = """INSERT INTO User (first_name, last_name, email, address, gamertag, profile_picture,
    password, role)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

    result = DbService.execute(query, 'c', payload['first_name'], payload['last_name'], payload['email'],
                               payload['address'], payload['gamertag'], payload['profile_picture'], payload['password'],
                               payload['role'])
    if result:
        return retrieve_user(payload['gamertag'])
    else:
        return {'err': 'The user could not be created'}


def retrieve_user(gamertag):
    query = """SELECT *
                FROM User
                WHERE gamertag = %s;"""

    result = DbService.execute(query, 'r', gamertag)
    if len(result):
        result = result[0]
        return User(result)
    else:
        return {'message': "No user was found with that gamertag"}


def get_users():
    query = """SELECT * FROM User;"""

    result = DbService.execute(query, 'r')
    response = []
    for row in result:
        response.append(User(row))

    return response


def update_user(payload):
    query = """UPDATE User
                SET first_name = %s,
                    last_name = %s,
                    email = %s,
                    gamertag = %s,
                    address = %s,
                    profile_picture = %s
                WHERE id = %s;"""

    rows_affected = DbService.execute(query, 'u', payload['first_name'], payload['last_name'], payload['email'],
                                      payload['gamertag'], payload['address'], payload['profile_picture'],
                                      payload['id'])
    if not rows_affected:
        return {'message': 'No users were affected'}

    else:
        return __retrieve_user_by_id(payload['id'])


def delete_user(id):
    query = """DELETE FROM User WHERE id = %s;"""
    response = __retrieve_user_by_id(id)

    if (not type(response) is User) and 'err' in response.keys():
        return response

    result = DbService.execute(query, 'd', id)

    if result:
        return response
    else:
        return {'message': 'No users with were affected'}


def login_user(payload):
    query = "SELECT email, password, gamertag FROM User WHERE email = %s AND password = %s;"

    result = DbService.execute(query, 'r', payload['email'], payload['password'])

    if len(result):
        payload['gamertag'] = result[0][2]
        return payload
    else:
        return {'err': "No user was found with those credentials"}


def get_user_role_gamertag(email):
    query = 'SELECT role, gamertag FROM User WHERE email = %s;'

    result = DbService.execute(query, 'r', email)[0]

    return {
        'role': result[0],
        'gamertag': result[1]
    }


def __retrieve_user_by_id(id):
    query = """SELECT *
                FROM User
                WHERE id = %s;"""

    result = DbService.execute(query, 'r', id)
    if len(result):
        return User(result[0])

    else:
        return {'err': 'No user with that id exists'}


def check_email_gamertag_duplication(id, email, gamertag,):
    query = """SELECT email, gamertag FROM USER WHERE (email = %s OR gamertag = %s) AND id != %s"""

    result = DbService.execute(query, 'r', email, gamertag, id)
    return len(result)

