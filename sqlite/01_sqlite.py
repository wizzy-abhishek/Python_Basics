import sqlite3 as sql

connection = sql.connect('mydb.db')
cursor = connection.cursor()

cursor.execute('''
    Create Table if not exists employee(
        id Integer Primary Key,
        name Text not null,
        dept text not null        
    )''')

connection.commit()

cursor.execute("""
    Insert into employee(name, dept) values ("Abhishek", "AI Engineer")
""")

connection.commit()

cursor.execute("Select * from employee")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("DROP table employee")
connection.commit()

cursor.close()
connection.close()