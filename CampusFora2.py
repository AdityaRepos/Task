from flask import Flask, request, jsonify
from flask_cors import CORS #this also
import sqlite3

app = Flask(__name__)
CORS(app) # add this line to enable CORS for your Flask app(this one i asked on chatgpt)
DB_NAME = 'posts.db'

with sqlite3.connect(DB_NAME) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, body TEXT)')

@app.route('/newpost', methods=['POST'])
def new_post():
    title = request.form.get('title')
    body = request.form.get('body')

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('INSERT INTO posts (title, body) VALUES (?, ?)', (title, body))

    return jsonify({'message': 'Post added successfully.'}) #once an error occured related json (this one i asked on chatgpt)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
