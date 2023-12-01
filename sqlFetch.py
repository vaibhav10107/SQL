import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the SELECT query to retrieve all columns
cursor.execute("SELECT Name, age, place  FROM Employees")

# Retrieve all rows of the result set
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print(rows)

# Close the connection
conn.close()
