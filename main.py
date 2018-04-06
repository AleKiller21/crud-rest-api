from flask import Flask, json, request
from services.UserService import add_user, get_user, get_all_users, modify_user, remove_user

app = Flask(__name__)


@app.route('/user/add', methods=['POST'])
def add():
    return add_user(request.json)


@app.route('/user/<gamertag>')
def user(gamertag):
    return json.dumps(get_user(gamertag))


@app.route('/users')
def users():
    return json.dumps(get_all_users())


@app.route('/users/update', methods=['POST'])
def update():
    return modify_user(request.json)


@app.route('/users/delete', methods=['POST'])
def delete():
    return remove_user(request.json)


if __name__ == '__main__':
    app.run(debug=True)
