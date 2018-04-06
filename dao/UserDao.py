from services.DbService import DbService


def create_user(first_name, last_name, email, gamertag, address=''):
    query = """INSERT INTO User (first_name, last_name, email, address, gamertag)
                VALUES (%s, %s, %s, %s, %s);"""

    result = DbService.execute(query, 'c', first_name, last_name, email, address, gamertag)
    if result:
        return retrieve_user(gamertag)
    else:
        return {'message': 'The user could not be created'}


def retrieve_user(gamertag):
    query = """SELECT *
                FROM User
                WHERE gamertag = %s;"""

    result = DbService.execute(query, 'r', gamertag)
    if len(result):
        result = result[0]
        return {
            'id': result[0],
            'first_name': result[1],
            'last_name': result[2],
            'email': result[3],
            'address': result[4],
            'gamertag': result[5]
        }
    else:
        return {'message': "No user was found with that gamertag"}


def get_users():
    query = """SELECT * FROM User;"""

    result = DbService.execute(query, 'r')
    response = []
    for row in result:
        response.append({
            'id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'email': row[3],
            'address': row[4],
            'gamertag': row[5]
        })

    return response


def update_user(id, first_name, last_name, email, gamertag, address):
    query = """UPDATE User
                SET first_name = %s,
                    last_name = %s,
                    email = %s,
                    gamertag = %s,
                    address = %s
                WHERE id = %s;"""

    rows_affected = DbService.execute(query, 'u', first_name, last_name, email, gamertag, address, id)
    if not rows_affected:
        return {'message': 'No users with were affected'}

    else:
        return __retrieve_user_by_id(id)


def delete_user(id):
    query = """DELETE FROM User WHERE id = %s;"""

    return DbService.execute(query, 'd', id)


def __retrieve_user_by_id(id):
    query = """SELECT *
                FROM User
                WHERE id = %s;"""

    result = DbService.execute(query, 'r', id)[0]
    return {
        'id': result[0],
        'first_name': result[1],
        'last_name': result[2],
        'email': result[3],
        'address': result[4],
        'gamertag': result[5]
    }