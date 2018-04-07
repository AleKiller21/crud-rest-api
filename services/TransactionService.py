from services.UtilService import __check_fields_existance_in_payload
from services.MessageService import missing_fields_request
from dao.TransactionDao import create_order, retrieve_transaction, get_transactions
from beans.TransactionBean import Transaction


def add_order(payload):
    if __check_fields_existance_in_payload(payload, 'User_id', 'Game_id'):
        return __transaction_to_json(create_order(payload))
    else:
        return missing_fields_request


def get_transaction(order_number):
    return __transaction_to_json(retrieve_transaction(order_number))


def get_all_transactions():
    result = get_transactions()
    response = []
    for transaction in result:
        response.append(__transaction_to_json(transaction))

    return response


def __transaction_to_json(order):
    if type(order) is Transaction:
        return {
            'order_number': order.order_number,
            'User_id': order.user_id,
            'Game_id': order.game_id
        }
    else:
        return order
