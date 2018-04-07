from services.DbService import DbService
from beans.TransactionBean import Transaction


def create_order(payload):
    query = """INSERT INTO Transaction (User_id, Game_id) VALUES (%s, %s);"""

    result = DbService.execute(query, 'c', payload['User_id'], payload['Game_id'])
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
