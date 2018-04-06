from flask import Flask, json, request
from services.UserService import add_user, get_user, get_all_users, modify_user, remove_user
from services.ResponseService import set_headers

app = Flask(__name__)


@app.route('/user/add', methods=['POST'])
def add():
    return set_headers(json.dumps(add_user(request.json)), {'Content-Type': 'application/json'})


@app.route('/user/<gamertag>')
def user(gamertag):
    return set_headers(json.dumps(get_user(gamertag)), {'Content-Type': 'application/json'})


@app.route('/users')
def users():
    return set_headers(json.dumps(get_all_users()), {'Content-Type': 'application/json'})


@app.route('/users/update', methods=['POST'])
def update():
    return set_headers(json.dumps(modify_user(request.json)), {'Content-Type': 'application/json'})
    # return modify_user(request.json)


@app.route('/users/delete', methods=['POST'])
def delete():
    return set_headers(json.dumps(remove_user(request.json)), {'Content-Type': 'application/json'})
    # return remove_user(request.json)


if __name__ == '__main__':
    app.run(debug=True)
