import sqlite3

def insert_data():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quotes (author, quote) VALUES (?, ?)", ("Test User", "This is a test quote."))
    cursor.execute("INSERT INTO quotes (author, quote) VALUES (?, ?)", ("Another Author", "Another test entry."))
    conn.commit()
    conn.close()
    print("Test data inserted.")

if __name__ == "__main__":
    insert_data()