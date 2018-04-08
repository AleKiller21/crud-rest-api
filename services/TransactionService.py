from services.UtilService import check_fields_existance_in_payload
from services.MessageService import missing_fields_request
from dao.TransactionDao import create_order, retrieve_transactions_by_game_id, retrieve_transaction_by_order_number, \
    retrieve_transactions_by_user_id, get_transactions, update_transaction
from beans.TransactionBean import Transaction


def add_order(payload):
    if check_fields_existance_in_payload(payload, 'user_id', 'game_id', 'total'):
        return __transaction_to_json(create_order(payload))
    else:
        return missing_fields_request


def get_transaction_by_order_number(order_number):
    return __transaction_to_json(retrieve_transaction_by_order_number(order_number))


def get_transactions_by_user_id(user_id):
    return process_transactions_projection(retrieve_transactions_by_user_id(user_id))


def get_transactions_by_game_id(game_id):
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
