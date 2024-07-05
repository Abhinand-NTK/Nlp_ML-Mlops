import sqlite3

connection_db = sqlite3.connect('sqlite.db')
connection_db

# Making the database using the cursor object.

cursor_ob = connection_db.cursor()

#Create a table using the Cursor object

cursor_ob.execute('''
Create table if Not Exists employee(
                  id Integer Primary Key,
                  Name Text Not Null,
                  age Integer,
                  departmetn text
                  )
''')

## Commit the changes in the table

connection_db.commit()

connection_db.execute(
    '''
    select * from employee
    '''
)

## Inserting data into the data base

cursor_ob.execute('''
    insert into employee(name,age,departmetn) values('Abhinand','26','Python Developer')
''')

connection_db.commit()

cursor_ob.execute(
    '''
    select * from employee
    '''
)

rows = cursor_ob.fetchall()

for row in rows:
    print(row)

## Update the data into the table 

cursor_ob.execute('''
                  update employee set age = 27 where name ='Abhinand'
                  ''')

connection_db.commit()


cursor_ob.execute(
    '''
    select * from employee
    '''
)

rows = cursor_ob.fetchall()

for row in rows:
    print(row)

# Delete the data from the table

cursor_ob.execute(
    '''
    Delete from employee where age = 27 and age =26
    '''
)

connection_db.commit()

cursor_ob.execute(
    '''
    select * from employee
    '''
)

rows = cursor_ob.fetchall()

for row in rows:
    print(row)
