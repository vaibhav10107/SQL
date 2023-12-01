import sqlite3
# Connect to a database (creates if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
# Creating a table
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                   ID INTEGER PRIMARY KEY,
                   Name TEXT,
                   Age INTEGER,
                   Department TEXT,
                   Place TEXT)''')

# Inserting data
cursor.execute("INSERT INTO Employees (Name, Age, Department, Place) VALUES (?, ?, ?,?)", ('John Doe', 30, 'Sales','Action To Action'))

# Fetching data
cursor.execute("SELECT * FROM Employees")
rows = cursor.fetchall()  # Fetch all rows
for row in rows:
    print(row)
conn.commit()
conn.close()
