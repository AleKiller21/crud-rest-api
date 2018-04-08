from services.DbService import DbService
from beans.TransactionBean import Transaction


def create_order(payload):
    query = """INSERT INTO Transaction (user_id, game_id, total) VALUES (%s, %s, %s);"""

    result = DbService.execute(query, 'c', payload['user_id'], payload['game_id'], payload['total'])
    if result:
        return {'message': 'The order was a success'}
    else:
        return {'err': 'The order could not be processed'}


def get_transactions():
    query = """SELECT * FROM Transaction;"""
    result = DbService.execute(query, 'r')
    return __process_multiple_transactions_result(result)


def update_transaction(payload):
    query = """UPDATE Transaction
                SET status = %s
                WHERE order_number = %s;"""

    rows_affected = DbService.execute(query, 'u', payload['status'], payload['order_number'])
    if not rows_affected:
        return {'message': 'No orders were affected'}

    else:
        return retrieve_transaction_by_order_number(payload['order_number'])


def retrieve_transactions_by_user_id(user_id):
    query = """SELECT *
                FROM Transaction
                WHERE user_id = %s;"""

    result = DbService.execute(query, 'r', user_id)
    return __process_multiple_transactions_result(result)


def retrieve_transactions_by_game_id(game_id):
    query = """SELECT *
                FROM Transaction
                WHERE game_id = %s;"""

    result = DbService.execute(query, 'r', game_id)
    return __process_multiple_transactions_result(result)


def retrieve_transaction_by_order_number(order_number):
    query = """SELECT *
                FROM Transaction
                WHERE order_number = %s;"""

    result = DbService.execute(query, 'r', order_number)
    if len(result):
        return Transaction(result[0])
    else:
        return {'message': 'No order with that order_number exists'}


def __process_multiple_transactions_result(dao_result):
    response = []
    for row in dao_result:
        response.append(Transaction(row))

    if not len(response):
        return {'message': 'No orders were found'}

    return response
