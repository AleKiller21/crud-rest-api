from services.UtilService import check_fields_existance_in_payload
from services.UserService import is_user_admin
import services.AuthService as AuthService
import services.MessageService as MessageService
from dao.GameDao import create_game, retrieve_game, get_games, update_game, delete_game


def add_game(payload, headers):
    try:
        auth = AuthService.get_user_email_from_token(headers)
    except Exception:
        return MessageService.authentication_required

    try:
        if not is_user_admin(auth):
            return MessageService.lack_of_privilege

        if check_fields_existance_in_payload(payload, 'name', 'developer', 'publisher', 'price', 'description', 'image'):
            game = create_game(payload)

            if game:
                return MessageService.generate_success_message('', game.to_dictionary())
            else:
                return MessageService.generate_custom_message('The game could not be created', 500)
        else:
            return MessageService.missing_fields_request

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def get_game(name):
    try:
        game = retrieve_game(name)
        if game:
            return MessageService.generate_success_message('', game.to_dictionary())
        else:
            return MessageService.generate_custom_message('The game was not found', {})

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def get_all_games():
    try:
        result = get_games()
        games = []
        for game in result:
            games.append(game.to_dictionary())

        if len(games):
            return MessageService.generate_success_message('', games)
        else:
            return MessageService.generate_custom_message('No games were found', [])

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def modify_game(payload, headers):
    try:
        auth = AuthService.get_user_email_from_token(headers)
    except Exception:
        return MessageService.authentication_required

    try:
        if not is_user_admin(auth):
            return MessageService.lack_of_privilege

        if check_fields_existance_in_payload(payload, 'id', 'name', 'developer', 'publisher', 'description', 'price'):
            game = update_game(payload)

            if game:
                return MessageService.generate_success_message('', game.to_dictionary())
            else:
                return MessageService.generate_custom_message('No game with that id was found', {})
        else:
            return MessageService.missing_fields_request

    except Exception as e:
        MessageService.generate_internal_server_error(e)


def remove_game(payload, headers):
    try:
        auth = AuthService.get_user_email_from_token(headers)
    except Exception:
        return MessageService.authentication_required

    try:
        if not is_user_admin(auth):
            return MessageService.lack_of_privilege

        if check_fields_existance_in_payload(payload, 'id'):
            game = delete_game(payload['id'])

            if game:
                return MessageService.generate_success_message('', game.to_dictionary())
            else:
                return MessageService.generate_custom_message('The game could not be removed', {})
        else:
            return MessageService.missing_fields_request

    except Exception as e:
        return MessageService.generate_internal_server_error(e)
