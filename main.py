from flask import Flask, json, request
import services.UserService as userService
import services.GameService as gameService
import services.TransactionService as transactionService
from services.ResponseService import set_headers
from services.AuthService import authenticate

app = Flask(__name__)


@app.before_request
def before_request():
    if request.method == 'OPTIONS':
        if 'Access-Control-Request-Headers' in request.headers:
            if 'authorization' in request.headers['Access-Control-Request-Headers'].split(','):
                return set_headers({}, {})

    result = authenticate(request.endpoint, request.headers)
    if result['code'] != 200:
        return json.dumps(result)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Content-Type', 'application/json')

    if len(response.response):
        response.status = str(json.loads(response.response[0].decode('utf-8'))['code'])

    return response


@app.route('/user', methods=['POST', 'PUT'])
def add_user():
    if request.method == 'POST':
        return json.dumps(userService.add_user(request.json))
    else:
        return json.dumps(userService.modify_user(request.json))


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    return json.dumps(userService.remove_user(id))


@app.route('/user/<gamertag>')
def get_user(gamertag):
    return json.dumps(userService.get_user(gamertag, request.headers['Authorization']))


@app.route('/users')
def get_users():
    return json.dumps(userService.get_all_users())


@app.route('/game', methods=['POST', 'PUT'])
def add_game():
    if request.method == 'POST':
        return json.dumps(gameService.add_game(request.json))
    else:
        return json.dumps(gameService.modify_game(request.json))


@app.route('/game/<int:id>', methods=['DELETE'])
def delete_game(id):
    return json.dumps(gameService.remove_game(id))


@app.route('/game/<name>')
def get_game(name):
    return json.dumps(gameService.get_game(name))


@app.route('/games')
def get_games():
    return json.dumps(gameService.get_all_games(request.args.get('name')))


@app.route('/order', methods=['POST', 'PUT'])
def add_order():
    if request.method == 'POST':
        return json.dumps(transactionService.add_order(request.json))
    else:
        return json.dumps(transactionService.modify_transaction_status(request.json))


@app.route('/order/<int:order_number>')
def get_order_by_order_number(order_number):
    return json.dumps(transactionService.get_transaction_by_order_number(order_number))


@app.route('/orders/game/<int:game_id>')
def get_order_by_game_id(game_id):
    return json.dumps(transactionService.get_transactions_by_game_id(game_id))


@app.route('/orders/user')
def get_order_by_user():
    return json.dumps(transactionService.get_transactions_by_user(request.headers['Authorization']))


@app.route('/orders')
def get_orders():
    return json.dumps(transactionService.get_all_transactions())


@app.route('/login', methods=['POST'])
def login():
    return json.dumps(userService.login(request.json))


if __name__ == '__main__':
    app.run(debug=True)
