import sqlite3

connect = sqlite3.connect("homework.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL
)
""")

connect.commit()
def add_book(title, author, price):
    cursor.execute(
        "INSERT INTO books (title, author, price) VALUES (?, ?, ?)",
        (title, author, price)
    )
    connect.commit()

    add_book("1984", "George Orwell", 9.99)
    add_book("The Alchemist", "Paulo Coelho", 7.50)



def get_all_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()

    books = get_all_books()
    for book in books:
        # print(books)
        print(book)

