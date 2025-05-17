import sqlite3

def remove_data():
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quotes WHERE quote LIKE '%test%'")
    conn.commit()
    conn.close()
    print("Test data removed.")

if __name__ == "__main__":
    remove_data()