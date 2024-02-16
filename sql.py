import sqlite3

## connect to sqlite
connection = sqlite3.connect("student.db")

## create a cursor object to insert record, create table, retrive
cursor = connection.cursor()

## create the table
table_info="""
Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

## insert some records

cursor.execute('''Insert into STUDENT values('Ratul', 'Data Science','A','100') ''')
cursor.execute('''Insert into STUDENT values('Anirban', 'Banking','A','60') ''')
cursor.execute('''Insert into STUDENT values('Bardhan', 'Banking','A','75') ''')
cursor.execute('''Insert into STUDENT values('Kundu', 'Web dev','A','80') ''')
cursor.execute('''Insert into STUDENT values('Dibya', 'Medical Science','A','80') ''')

## display all the records
print("the inserted records are ")

data = cursor.execute(''' Select * from STUDENT ''')

for row in data:
    print(row)

## close the connection
connection.commit()
connection.close()