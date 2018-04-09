from services.UtilService import check_fields_existance_in_payload
from services.UserService import is_user_admin
import services.AuthService as AuthService
import services.MessageService as MessageService
from dao.GameDao import create_game, retrieve_game, get_games, update_game, delete_game
from beans.GameBean import Game


def add_game(payload, headers):
    auth = AuthService.get_user_email_from_token(headers)

    if 'err' in auth.keys():
        return auth

    if not is_user_admin(auth):
        return MessageService.lack_of_privilege

    if check_fields_existance_in_payload(payload, 'name', 'developer', 'publisher', 'price', 'description'):
        return __game_to_json(create_game(payload))
    else:
        return MessageService.missing_fields_request


def get_game(name):
    return __game_to_json(retrieve_game(name))


def get_all_games():
    result = get_games()
    response = []
    for game in result:
        response.append(__game_to_json(game))

    return response


def modify_game(payload):
    if check_fields_existance_in_payload(payload, 'id', 'name', 'developer', 'publisher', 'description', 'price'):
        return __game_to_json(update_game(payload))
    else:
        return MessageService.missing_fields_request


def remove_game(payload):
    if check_fields_existance_in_payload(payload, 'id'):
        return __game_to_json(delete_game(payload['id']))
    else:
        return MessageService.missing_fields_request


def __game_to_json(game):
    if type(game) is Game:
        return game.to_dictionary()
    else:
        return game



