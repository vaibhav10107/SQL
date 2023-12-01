import streamlit as st
import sqlite3


conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                   ID INTEGER PRIMARY KEY,
                   Name TEXT,
                   Age INTEGER,
                   Department TEXT,
                   Place TEXT)''')


st.title('Employee Database')


name = st.text_input("Enter the Name:")
age = st.number_input("Enter the Age:", value=0)
dep = st.text_input("Enter the Department:")
place = st.text_input("Enter the Place:")


if st.button('Add Employee'):
    cursor.execute("INSERT INTO Employees (Name, Age, Department, Place) VALUES (?, ?, ?, ?)", (name, age, dep, place))
    conn.commit()
    st.success('Employee added successfully!')


st.subheader('Current Employees')
cursor.execute("SELECT * FROM Employees")
rows = cursor.fetchall()


for row in rows:
    st.write(row)


st.subheader('Edit Employee')
edit_name = st.text_input("Enter the Name to edit:")
new_age = st.number_input("Enter the New Age:", value=0)
new_dep = st.text_input("Enter the New Department:")
new_place = st.text_input("Enter the New Place:")

if st.button('Edit'):
    cursor.execute("UPDATE Employees SET Age=?, Department=?, Place=? WHERE Name=?", (new_age, new_dep, new_place, edit_name))
    conn.commit()
    st.info(f"Edited employee with name '{edit_name}'")


st.subheader('Delete Employee')
delete_name = st.text_input("Enter the Name to delete:")
if st.button('Delete'):
    cursor.execute("DELETE FROM Employees WHERE Name = ?", (delete_name,))
    conn.commit()
    st.warning(f"Deleted employee with name '{delete_name}'")


conn.close()
