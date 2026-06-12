import sqlite3

# Connect to database
conn = sqlite3.connect("academy.db")
cursor = conn.cursor()

# Student data
students = [
    (1, "Rahul", 20, "Mumbai", "Python", 88),
    (2, "Priya", 21, "Pune", "SQL", 75),
    (3, "Amit", 19, "Nashik", "Python", 92),
    (4, "Sneha", 22, "Mumbai", "Power BI", 67),
    (5, "Karan", 20, "Pune", "SQL", 81),
    (6, "Neha", 21, "Nashik", "Python", 59),
    (7, "Arjun", 20, "Mumbai", "SQL", 95),
    (8, "Pooja", 22, "Pune", "Power BI", 73),
    (9, "Vikram", 19, "Nashik", "Python", 84),
    (10, "Meera", 20, "Mumbai", "SQL", 62),
    (11, "Rohan", 21, "Pune", "Python", 77),
    (12, "Kavya", 22, "Nashik", "Power BI", 90),
    (13, "Ankit", 20, "Mumbai", "SQL", 55),
    (14, "Simran", 21, "Pune", "Python", 86),
    (15, "Deepak", 22, "Nashik", "SQL", 71)
]

# Insert all records
cursor.executemany(
    """
    INSERT INTO students
    (id, name, age, city, course, marks)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    students
)

# Save changes
conn.commit()

# Close connection
conn.close()

print("15 student records inserted successfully!")