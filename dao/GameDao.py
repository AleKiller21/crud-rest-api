from services.DbService import DbService
from beans.GameBean import Game


def create_game(payload):
    query = """INSERT INTO Game (name, developer, publisher, price, description)
                VALUES (%s, %s, %s, %s, %s);"""

    result = DbService.execute(query, 'c', payload['name'], payload['developer'], payload['publisher'],
                               payload['price'], payload['description'])
    if result:
        return retrieve_game(payload['name'])
    else:
        return {'err': 'The game could not be created'}


def retrieve_game(name):
    query = """SELECT *
                FROM Game
                WHERE name = %s;"""

    result = DbService.execute(query, 'r', name)
    if len(result):
        result = result[0]
        return Game(result)
    else:
        return {'message': "No game was found with that name"}
