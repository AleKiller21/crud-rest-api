from services.UtilService import check_fields_existance_in_payload
import services.MessageService as MessageService
import dao.TransactionDao as TransactionDao


def add_order(payload):
    try:
        if check_fields_existance_in_payload(payload, 'user_id', 'game_id', 'total'):
            order = TransactionDao.create_order(payload)

            if order:
                return MessageService.generate_success_message('success', {})
            else:
                return MessageService.generate_custom_message('The order could not be created', 500, {})
        else:
            return MessageService.missing_fields_request

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def get_transaction_by_order_number(order_number):
    try:
        order = TransactionDao.retrieve_transaction_by_order_number(order_number)
        if order:
            return MessageService.generate_success_message('', order.to_dictionary())
        else:
            return MessageService.generate_custom_message('No order with that order number could be found', {})

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def get_transactions_by_user_id(id):
    try:
        transactions = TransactionDao.retrieve_transactions_by_user_email(id)
        if not len(transactions):
            return MessageService.generate_custom_message('No orders were found', [])

        return MessageService.generate_success_message('', transactions)

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def get_transactions_by_game_id(game_id):
    try:
        orders = TransactionDao.retrieve_transactions_by_game_id(game_id)

        if len(orders):
            return MessageService.generate_success_message('', process_transactions_projection())
        else:
            return MessageService.generate_custom_message('No orders were found', [])

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def get_all_transactions():
    try:
        orders = TransactionDao.get_transactions()

        if len(orders):
            return MessageService.generate_success_message('', orders)
        else:
            return MessageService.generate_custom_message('No orders were found', [])

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def modify_transaction_status(payload):
    if not check_fields_existance_in_payload(payload, 'status', 'order_number'):
        return MessageService.missing_fields_request

    try:
        order = TransactionDao.update_transaction(payload)
        if order:
            return MessageService.generate_success_message('', order.to_dictionary())
        else:
            return MessageService.generate_custom_message('the order could not be updated', {})

    except Exception as e:
        return MessageService.generate_internal_server_error(e)


def process_transactions_projection(dao_result):
    response = []
    for transaction in dao_result:
        response.append(transaction.to_dictionary())

    return response
