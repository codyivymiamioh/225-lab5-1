from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB_NAME = 'quotes.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, author TEXT, quote TEXT)")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_quote():
    author = request.form['author']
    quote = request.form['quote']
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO quotes (author, quote) VALUES (?, ?)", (author, quote))
    return redirect('/quotes')

@app.route('/quotes')
def show_quotes():
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute("SELECT author, quote FROM quotes").fetchall()
    return render_template('quotes.html', quotes=rows)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)