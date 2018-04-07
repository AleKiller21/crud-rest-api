from services.DbService import DbService
from beans.TransactionBean import Transaction


def create_order(payload):
    query = """INSERT INTO Transaction (user_id, game_id) VALUES (%s, %s);"""

    result = DbService.execute(query, 'c', payload['user_id'], payload['game_id'])
    if result:
        return {'message': 'The order was a success'}
    else:
        return {'err': 'The order could not be processed'}


def retrieve_transaction(order_number):
    query = """SELECT *
                FROM Transaction
                WHERE order_number = %s;"""

    result = DbService.execute(query, 'r', order_number)
    if len(result):
        result = result[0]
        return Transaction(result)
    else:
        return {'message': "No order was found with that order number"}


def get_transactions():
    query = """SELECT * FROM Transaction;"""

    result = DbService.execute(query, 'r')
    response = []
    for row in result:
        response.append(Transaction(row))

    return response


def update_transaction(payload):
    query = """UPDATE Transaction
                SET status = %s
                WHERE order_number = %s;"""

    rows_affected = DbService.execute(query, 'u', payload['status'], payload['order_number'])
    if not rows_affected:
        return {'message': 'No orders were affected'}

    else:
        return __retrieve_transaction_by_ordernumber(payload['order_number'])


def __retrieve_transaction_by_ordernumber(order_number):
    query = """SELECT *
                FROM Transaction
                WHERE order_number = %s;"""

    result = DbService.execute(query, 'r', order_number)
    if len(result):
        return Transaction(result[0])

    else:
        return {'err': 'No order with that order number exists'}
