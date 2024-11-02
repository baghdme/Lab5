from database import *

if __name__ == '__main__':
    create_db_table()

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    conn.close()
    if users:
        # Convert list of tuples to list of dictionaries
        users_list = [{description[0]: value for description, value in zip(cur.description, user)} for user in users]
        return jsonify(users_list)
    else:
        return jsonify([])  # Return an empty list if no users are found

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cur.fetchone()
    conn.close()
    if user:
        # Convert row to dictionary
        user_dict = {description[0]: user[index] for index, description in enumerate(cur.description)}
        return jsonify(user_dict)
    else:
        return 'User not found', 404

@app.route('/api/users', methods=['POST'])
def add_user():
    user = request.get_json()
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)",
                (user['name'], user['email'], user['phone'], user['address'], user['country']))
    conn.commit()
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.get_json()
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id = ?",
                (user['name'], user['email'], user['phone'], user['address'], user['country'], user_id))
    conn.commit()
    return jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    conn.commit()
    return {'message': 'User deleted successfully'}, 200

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
