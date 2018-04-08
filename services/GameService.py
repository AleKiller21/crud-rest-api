from services.UtilService import __check_fields_existance_in_payload
from services.MessageService import missing_fields_request
from dao.GameDao import create_game, retrieve_game, get_games, update_game, delete_game
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


def modify_game(payload):
    if __check_fields_existance_in_payload(payload, 'id', 'name', 'developer', 'publisher', 'description', 'price'):
        return __game_to_json(update_game(payload))
    else:
        return missing_fields_request


def remove_game(payload):
    if __check_fields_existance_in_payload(payload, 'id'):
        return __game_to_json(delete_game(payload['id']))
    else:
        return missing_fields_request


def __game_to_json(game):
    if type(game) is Game:
        return game.to_dictionary()
    else:
        return game



