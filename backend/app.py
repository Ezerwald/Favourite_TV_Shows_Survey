# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table if it doesn't exist
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            address TEXT,
            dob TEXT,
            gender TEXT,
            favorite_shows TEXT,
            show_types TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/api/submit-survey', methods=['POST'])
def submit_survey():
    data = request.json
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO survey (first_name, last_name, email, address, dob, gender, favorite_shows, show_types)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['firstName'],
        data['lastName'],
        data['email'],
        data['address'],
        data['dob'],
        data['gender'],
        ', '.join(data['favoriteShows']),
        ', '.join(data['showTypes'])
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Survey submitted successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
