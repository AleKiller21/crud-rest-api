from services.DbService import DbService
from beans.UserBean import User


def create_user(payload):
    query = """INSERT INTO User (first_name, last_name, email, address, gamertag, profile_picture)
                VALUES (%s, %s, %s, %s, %s, %s);"""

    result = DbService.execute(query, 'c', payload['first_name'], payload['last_name'], payload['email'],
                               payload['address'], payload['gamertag'], payload['profile_picture'])
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
                                      payload['gamertag'], payload['address'], payload['profile_picture'], payload['id'])
    if not rows_affected:
        return {'message': 'No users with were affected'}

    else:
        return __retrieve_user_by_id(payload['id'])


def delete_user(id):
    query = """DELETE FROM User WHERE id = %s;"""
    response = __retrieve_user_by_id(id)

    if 'err' in response.keys():
        return response

    result = DbService.execute(query, 'd', id)

    if result:
        return response
    else:
        return {'message': 'No users with were affected'}


def __retrieve_user_by_id(id):
    query = """SELECT *
                FROM User
                WHERE id = %s;"""

    result = DbService.execute(query, 'r', id)
    if len(result):
        result = result[0]
        return {
            'id': result[0],
            'first_name': result[1],
            'last_name': result[2],
            'email': result[3],
            'address': result[4],
            'gamertag': result[5],
            'profile_picture': result[6]
        }

    else:
        return {'err': 'No user with that id exists'}
