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

# Sukuriame duomenų bazę ir lentelę
def create_table():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)''')
    conn.commit()
    conn.close()

# Funkcija, kuri prideda įrašą į duomenų bazę
def add_note_to_db(content):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

# Funkcija, kuri išgauna visas įrašus iš duomenų bazės
def get_notes_from_db():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM notes")
    notes = c.fetchall()
    conn.close()
    return notes

create_table()  # Sukuriame lentelę, jei ji neegzistuoja

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note_content = request.form['note']
        add_note_to_db(note_content)
        return redirect(url_for('index'))
    else:
        notes = get_notes_from_db()
        return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)