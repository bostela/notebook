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

