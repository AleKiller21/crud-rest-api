from services.UtilService import check_fields_existance_in_payload
from services.MessageService import missing_fields_request, lack_of_privilege
from services.UserService import is_user_admin
from dao.TransactionDao import create_order, retrieve_transactions_by_game_id, retrieve_transaction_by_order_number, \
    retrieve_transactions_by_user_id, get_transactions, update_transaction
from beans.TransactionBean import Transaction
import services.AuthService as AuthService


def add_order(payload):
    if check_fields_existance_in_payload(payload, 'user_id', 'game_id', 'total'):
        result = create_order(payload)
        if 'err' in result.keys():
            return result
        else:
            return __transaction_to_json(result)
    else:
        return missing_fields_request


def get_transaction_by_order_number(order_number, headers):
    auth = AuthService.get_user_email_from_token(headers)

    if 'err' in auth.keys():
        return auth

    if not is_user_admin(auth):
        return lack_of_privilege

    return __transaction_to_json(retrieve_transaction_by_order_number(order_number))


def get_transactions_by_user_id(user_id):
    return process_transactions_projection(retrieve_transactions_by_user_id(user_id))


def get_transactions_by_game_id(game_id, headers):
    auth = AuthService.get_user_email_from_token(headers)

    if 'err' in auth.keys():
        return auth

    if not is_user_admin(auth):
        return lack_of_privilege

    return process_transactions_projection(retrieve_transactions_by_game_id(game_id))


def get_all_transactions():
    result = get_transactions()
    return process_transactions_projection(result)


def modify_transaction_status(payload):
    if check_fields_existance_in_payload(payload, 'status', 'order_number'):
        return __transaction_to_json(update_transaction(payload))
    else:
        return missing_fields_request


def process_transactions_projection(dao_result):
    response = []
    for transaction in dao_result:
        response.append(__transaction_to_json(transaction))

    return response


def __transaction_to_json(order):
    if type(order) is Transaction:
        return order.to_dictionary()
    else:
        return order
