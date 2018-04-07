from dao.GameDao import create_game, retrieve_game
from beans.GameBean import Game


def add_game(payload):
    if __check_fields_existance(payload, 'name', 'developer', 'publisher', 'price', 'description'):
        return __game_to_json(create_game(payload))
    else:
        return {'err': 'Missing fields in json'}


def __game_to_json(game):
    if type(game) is Game:
        return {
            'id': game.id,
            'name': game.name,
            'developer': game.developer,
            'publisher': game.publisher,
            'price': game.price,
            'description': game.description
        }
    else:
        return game


def __check_fields_existance(payload, *fields):
    if all(key in payload for key in fields):
        return True
