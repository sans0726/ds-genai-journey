import sqlite3
import pandas as pd

conn = sqlite3.connect("academy.db")

df = pd.read_sql("SELECT * FROM students", conn)

print(df)

conn.close()
print(df.head())
print(df.describe())
