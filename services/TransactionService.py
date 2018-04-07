from services.UtilService import __check_fields_existance_in_payload
from services.MessageService import missing_fields_request
from dao.TransactionDao import create_order, retrieve_transaction, get_transactions, update_transaction
from beans.TransactionBean import Transaction


def add_order(payload):
    if __check_fields_existance_in_payload(payload, 'user_id', 'game_id'):
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


def modify_transaction_status(payload):
    if __check_fields_existance_in_payload(payload, 'status', 'order_number'):
        return __transaction_to_json(update_transaction(payload))
    else:
        return missing_fields_request


def __transaction_to_json(order):
    if type(order) is Transaction:
        return {
            'order_number': order.order_number,
            'user_id': order.user_id,
            'game_id': order.game_id,
            'status': order.status
        }
    else:
        return order
