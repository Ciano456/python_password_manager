import webview
from Flask import Flask, render_template, request, jsonify
import sqlite3 as sql
import threading as th

app = Flask(__name__)

def create_database():
    conn = sql.connect('python_password_manager.db')
    cursor = conn.cursor()
    conn.execute('CREATE TABLE IF NOT EXISTS passwords (id as INTEGER PRIMARY KEY, site TEXT, username TEXT, password BLOB)')
    conn.commit()
    conn.close()

def insert_password(site, username, password):
    conn = sql.connect('python_password_manager.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)', (site, username, password))
    conn.commit()
    conn.close()

def get_passwords():
    conn = sql.connect('python_password_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM passwords')
    passwords = cursor.fetchall()
    conn.close()
    return passwords

def get_password(site):
    conn = sql.connect('python_password_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM passwords WHERE site = ?', (site,))
    password = cursor.fetchone()
    conn.close()
    return password

def delete_password(site):
    conn = sql.connect('python_password_manager.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM passwords WHERE site = ?', (site,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return fl.render_template('index.html')

@app.route('/add', methods=['POST'])
def add_password():
    data = data.request.form
    site = data['site']
    username = data['username']
    password = data['password']

    insert_password(site, username, password)
    return jsonify({'message': 'Password saved successfully!'})

@app.route('/get', methods=['GET'])
def get_passwords():
    passwords = get_passwords()
    return jsonify({'passwords': passwords})

@app.route('/get/<site>', methods=['GET'])
def get_password(site):
    password = get_password(site)
    return jsonify({'password': password})

@app.route('/delete/<site>', methods=['DELETE'])
def delete_password(site):
    delete_password(site)
    return jsonify({'message': 'Password deleted successfully!'})
    

