from services.DbService import DbService
from beans.UserBean import User


def create_user(payload):
    query = """INSERT INTO User (first_name, last_name, email, address, gamertag, profile_picture,
    password, role)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

    DbService.execute(query, 'c', payload['first_name'], payload['last_name'], payload['email'],
                      payload['address'], payload['gamertag'], payload['profile_picture'], payload['password'],
                      payload['role'])

    return retrieve_user(payload['gamertag'])


def retrieve_user(gamertag):
    query = """SELECT *
                FROM User
                WHERE gamertag = %s;"""

    result = DbService.execute(query, 'r', gamertag)
    if len(result):
        result = result[0]
        return User(result)
    else:
        return None


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
        return None

    else:
        return __retrieve_user_by_id(payload['id'])


def delete_user(id):
    query = """DELETE FROM User WHERE id = %s;"""
    response = __retrieve_user_by_id(id)

    if not response:
        return response

    result = DbService.execute(query, 'd', id)

    if result:
        return response
    else:
        return None


def login_user(payload):
    query = "SELECT id, role, gamertag FROM User WHERE email = %s AND password = %s;"

    result = DbService.execute(query, 'r', payload['email'], payload['password'])

    if len(result):
        return {'id': result[0][0], 'role': result[0][1], 'gamertag': result[0][2]}
    else:
        return None


def get_user_role(id):
    query = 'SELECT role FROM User WHERE id = %s;'

    result = DbService.execute(query, 'r', id)[0]

    if not len(result):
        return None

    return {
        'role': result[0]
    }


def __retrieve_user_by_id(id):
    query = """SELECT *
                FROM User
                WHERE id = %s;"""

    result = DbService.execute(query, 'r', id)
    if len(result):
        return User(result[0])

    else:
        return None


def check_email_gamertag_duplication(id, email, gamertag):
    query = """SELECT email, gamertag FROM USER WHERE (email = %s OR gamertag = %s) AND id != %s"""

    result = DbService.execute(query, 'r', email, gamertag, id)
    return len(result)
