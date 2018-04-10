from services.DbService import DbService
from beans.GameBean import Game


def create_game(payload):
    query = """INSERT INTO Game (name, developer, publisher, price, description, image)
                VALUES (%s, %s, %s, %s, %s, %s);"""

    DbService.execute(query, 'c', payload['name'], payload['developer'], payload['publisher'],
                      payload['price'], payload['description'], payload['image'])

    return retrieve_game(payload['name'])


def retrieve_game(name):
    query = """SELECT *
                FROM Game
                WHERE name = %s;"""

    result = DbService.execute(query, 'r', name)
    if len(result):
        result = result[0]
        return Game(result)
    else:
        return None


def get_games():
    query = """SELECT * FROM Game;"""

    result = DbService.execute(query, 'r')
    response = []
    for row in result:
        response.append(Game(row))

    return response


def update_game(payload):
    query = """UPDATE Game
                SET name = %s,
                    developer = %s,
                    publisher = %s,
                    price = %s,
                    description = %s,
                    image = %s
                WHERE id = %s;"""

    rows_affected = DbService.execute(query, 'u', payload['name'], payload['developer'], payload['publisher'],
                                      payload['price'], payload['description'], payload['image'], payload['id'])
    if not rows_affected:
        return None

    else:
        return __retrieve_game_by_id(payload['id'])


def delete_game(id):
    query = """DELETE FROM Game WHERE id = %s;"""
    response = __retrieve_game_by_id(id)

    if not response:
        return response

    result = DbService.execute(query, 'd', id)

    if result:
        return response
    else:
        return None


def __retrieve_game_by_id(id):
    query = """SELECT *
                FROM Game
                WHERE id = %s;"""

    result = DbService.execute(query, 'r', id)
    if len(result):
        return Game(result[0])

    else:
        return None
