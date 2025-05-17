import unittest
import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.init_db()

    def test_add_quote(self):
        with app.sqlite3.connect(app.DB_NAME) as conn:
            conn.execute("DELETE FROM quotes")
            conn.execute("INSERT INTO quotes (author, quote) VALUES (?, ?)", ("Test Author", "Test Quote"))
            result = conn.execute("SELECT * FROM quotes").fetchall()
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0][1], "Test Author")
            self.assertEqual(result[0][2], "Test Quote")

if __name__ == '__main__':
    unittest.main()