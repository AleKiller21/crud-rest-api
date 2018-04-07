from services.UtilService import __check_fields_existance_in_payload
from services.MessageService import missing_fields_request
from dao.TransactionDao import create_order
from beans.TransactionBean import Transaction


def add_order(payload):
    if __check_fields_existance_in_payload(payload, 'User_id', 'Game_id'):
        return __order_to_json(create_order(payload))
    else:
        return missing_fields_request


def __order_to_json(order):
    if type(order) is Transaction:
        return {
            'order_number': order.order_number,
            'User_id': order.User_id,
            'Game_id': order.Game_id
        }
    else:
        return order
