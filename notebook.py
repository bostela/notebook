from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Sukuriame failus, jei jie neegzistuoja
def create_files():
    users_file = os.path.join(app.root_path, 'users.txt')
    notes_file = os.path.join(app.root_path, 'notes.txt')
    for file in [users_file, notes_file]:
        if not os.path.exists(file):
            with open(file, 'w'):
                pass

# Funkcija, kuri skaito vartotojus iš failo
def read_users():
    users_file = os.path.join(app.root_path, 'users.txt')
    with open(users_file, 'r', encoding='utf-8') as file:
        users = file.readlines()
    return [user.strip() for user in users]

# Funkcija, kuri rašo vartotojus į failą
def write_user(username):
    users_file = os.path.join(app.root_path, 'users.txt')
    with open(users_file, 'a', encoding='utf-8') as file:
        file.write(username + '\n')

# Funkcija, kuri skaito užrašus iš failo
def read_notes():
    notes_file = os.path.join(app.root_path, 'notes.txt')
    with open(notes_file, 'r', encoding='utf-8') as file:
        notes = file.readlines()
    return [note.strip() for note in notes]

# Funkcija, kuri rašo užrašus į failą
def write_note(note_content):
    notes_file = os.path.join(app.root_path, 'notes.txt')
    with open(notes_file, 'a', encoding='utf-8') as file:
        file.write(note_content + '\n')

@app.route('/')
def index():
    notes = read_notes()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note_content = request.form['note']
    write_note(note_content)
    return redirect(url_for('index'))

@app.route('/users', methods=['GET'])
def get_users():
    users = read_users()
    return render_template('users.html', users=users)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.form['username']
    write_user(new_user)
    return redirect(url_for('get_users'))

if __name__ == '__main__':
    create_files()
    app.run(debug=True)