from services.UtilService import check_fields_existance_in_payload
import services.MessageService as MessageService
from dao.GameDao import create_game, retrieve_game, get_games, update_game, delete_game


def add_game(payload):
    try:
        if check_fields_existance_in_payload(payload, 'name', 'developer', 'publisher', 'price', 'description', 'image'):
            game = create_game(payload)
            return MessageService.generate_success_message('The game has been created', game.to_dictionary())
        else:
            return MessageService.missing_fields_request

    except Exception:
        return MessageService.generate_internal_server_error('The game could not be created')


def get_game(name):
    try:
        game = retrieve_game(name)
        if game:
            return MessageService.generate_success_message('', game.to_dictionary())
        else:
            return MessageService.generate_success_message('The game was not found', {})

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def get_all_games(name):
    try:
        result = get_games(name)
        games = []
        for game in result:
            games.append(game.to_dictionary())

        if len(games):
            return MessageService.generate_success_message('', games)
        else:
            return MessageService.generate_success_message('No games were found', [])

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def modify_game(payload):
    try:
        if check_fields_existance_in_payload(payload, 'id', 'name', 'developer', 'publisher', 'description', 'price'):
            game = update_game(payload)

            if game:
                return MessageService.generate_success_message('The game has been updated', game.to_dictionary())
            else:
                return MessageService.generate_success_message('The game was not updated', {})
        else:
            return MessageService.missing_fields_request

    except Exception as e:
        MessageService.generate_internal_server_error(e)


def remove_game(id):
    try:
        game = delete_game(id)
        if game:
            return MessageService.generate_success_message('The game has been deleted', game.to_dictionary())
        else:
            return MessageService.generate_internal_server_error('The game could not be removed')

    except Exception as e:
        return MessageService.generate_internal_server_error(e)
