import sqlite3

def init_db():
    conn = sqlite3.connect('quotes.db')
    conn.execute("CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, author TEXT, quote TEXT)")
    conn.close()

def insert_data():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quotes (author, quote) VALUES (?, ?)", ("Test User", "This is a test quote."))
    cursor.execute("INSERT INTO quotes (author, quote) VALUES (?, ?)", ("Another Author", "Another test entry."))
    conn.commit()
    conn.close()
    print("Test data inserted.")

if __name__ == "__main__":
    init_db()
    insert_data()