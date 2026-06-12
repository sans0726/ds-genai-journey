import sqlite3

conn = sqlite3.connect("academy.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT,
    course TEXT,
    marks INTEGER
)
""")

conn.commit()
conn.close()

print("Database and table created!")
