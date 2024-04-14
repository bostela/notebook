from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Create necessary files if they do not exist
def create_files():
    users_file = os.path.join(app.root_path, 'users.txt')
    notes_file = os.path.join(app.root_path, 'notes.txt')
    for file in [users_file, notes_file]:
        if not os.path.exists(file):
            with open(file, 'w'):
                pass

# Read users from file
def read_users():
    users_file = os.path.join(app.root_path, 'users.txt')
    with open(users_file, 'r', encoding='utf-8') as file:
        users = file.readlines()
    return [user.strip() for user in users]

# Write a new user to the file
def write_user(username):
    users_file = os.path.join(app.root_path, 'users.txt')
    with open(users_file, 'a', encoding='utf-8') as file:
        file.write(username + '\n')

# Read notes from file
def read_notes():
    notes_file = os.path.join(app.root_path, 'notes.txt')
    with open(notes_file, 'r', encoding='utf-8') as file:
        notes = file.readlines()
    return [note.strip() for note in notes]

# Write a new note to the file
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
    note_content = request.form.get('note')
    if note_content:  # Check if the note content is not empty
        write_note(note_content)
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_files()
    app.run(debug=True)



