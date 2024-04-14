from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Pavyzdiniai duomenys
users = ['John', 'Alice', 'Bob']
notes = ['Lorem ipsum', 'Dolor sit amet', 'Consectetur adipiscing elit']

# Maršrutas vartotojams (GET)
@app.route('/users', methods=['GET'])
def get_users():
    return render_template('users.html', users=users)

# Maršrutas užrašams (GET)
@app.route('/notes', methods=['GET'])
def get_notes():
    return render_template('notes.html', notes=notes)

# Maršrutas vartotojams (POST)
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.form['username']
    users.append(new_user)
    return redirect(url_for('get_users'))

# Maršrutas užrašams (POST)
@app.route('/notes', methods=['POST'])
def add_note():
    new_note = request.form['note']
    notes.append(new_note)
    return redirect(url_for('get_notes'))