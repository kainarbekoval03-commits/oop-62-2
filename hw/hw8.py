import sqlite3

conn = sqlite3.connect("relations.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")



cursor.execute("""
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
)
""")



cursor.execute("INSERT INTO authors (name) VALUES (?)", ("George Orwell",))
cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Fyodor Dostoevsky",))

cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ("1984", 1))
cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ("Animal Farm", 1))
cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ("Crime and Punishment", 2))

conn.commit()




def get_authors_with_books():
    cursor.execute("""
    SELECT authors.name, books.title
    FROM authors
    INNER JOIN books ON authors.id = books.author_id
    """)
    return cursor.fetchall()


def get_books_by_author(author_id):
    cursor.execute("""
    SELECT books.title
    FROM books
    INNER JOIN authors ON books.author_id = authors.id
    WHERE authors.id = ?
    """, (author_id,))
    return cursor.fetchall()



print("📚 Авторы и их книги:")
for row in get_authors_with_books():
    print(row)

print("\n📖 Книги автора с id = 1:")
for row in get_books_by_author(1):
    print(row)

conn.close()