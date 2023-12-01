import sqlite3

name =  input("Enter the Name: \n")
Age =  input("Enter the Age: \n")
Dep =  input("Enter the Department: \n")
place =  input("Enter the Place: \n")
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
cursor.execute("INSERT INTO Employees (Name, Age, Department, Place) VALUES (?, ?, ?,?)", (name, Age, Dep,place))

# Fetching data
cursor.execute("SELECT * FROM Employees")
rows = cursor.fetchall()  # Fetch all rows
for row in rows:
    print(row)
conn.commit()
conn.close()
