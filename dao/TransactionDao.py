from services.DbService import DbService
from beans.TransactionBean import Transaction


def create_order(payload):
    query = """INSERT INTO Transaction (user_id, game_id, total) VALUES (%s, %s, %s);"""

    return DbService.execute(query, 'c', payload['user_id'], payload['game_id'], payload['total'])


def get_transactions():
    query = """SELECT * FROM Transaction;"""
    rows = DbService.execute(query, 'r')

    return __get_personalized_transactions(rows)


def update_transaction(payload):
    query = """UPDATE Transaction
                SET status = %s
                WHERE order_number = %s;"""

    rows_affected = DbService.execute(query, 'u', payload['status'], payload['order_number'])

    if not rows_affected:
        return None
    else:
        return retrieve_transaction_by_order_number(payload['order_number'])


def retrieve_transactions_by_user(id):
    transactions_query = """SELECT *
                        FROM Transaction
                        WHERE user_id = %s;"""

    rows = DbService.execute(transactions_query, 'r', id)
    return __get_personalized_transactions(rows)


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
        return None


def __process_multiple_transactions_result(dao_result):
    response = []
    for row in dao_result:
        response.append(Transaction(row))

    return response


def __get_personalized_transactions(order_rows):
    orders = []

    print(order_rows)
    for row in order_rows:
        user_query = """SELECT gamertag FROM User WHERE id = %s"""
        game_query = """SELECT name FROM Game WHERE id = %s"""
        user = DbService.execute(user_query, 'r', row[1])
        game = DbService.execute(game_query, 'r', row[2])

        order = Transaction(row).to_dictionary()
        order['gamertag'] = user[0][0]
        order['game_name'] = game[0][0]
        orders.append(order)

    print(orders)
    return orders
