from services.UtilService import __check_fields_existance_in_payload
from services.MessageService import missing_fields_request
from dao.GameDao import create_game, retrieve_game, get_games
from beans.GameBean import Game


def add_game(payload):
    if __check_fields_existance_in_payload(payload, 'name', 'developer', 'publisher', 'price', 'description'):
        return __game_to_json(create_game(payload))
    else:
        return missing_fields_request


def get_game(name):
    return __game_to_json(retrieve_game(name))


def get_all_games():
    result = get_games()
    response = []
    for game in result:
        response.append(__game_to_json(game))

    return response


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



