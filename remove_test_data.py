import sqlite3

def init_db():
    conn = sqlite3.connect('quotes.db')
    conn.execute("CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, author TEXT, quote TEXT)")
    conn.close()

def remove_data():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quotes WHERE quote LIKE '%test%'")
    conn.commit()
    conn.close()
    print("Test data removed.")

if __name__ == "__main__":
    init_db()
    remove_data()