# c:\users\kshaik\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin'
)
# print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE pythonprgm")
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
'''
################
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='pythonprgm'
)
mycursor = mydb.cursor()
# mycursor.execute('CREATE TABLE Customers(name VARCHAR(20),address VARCHAR(100))')
#############
mycursor.execute('show tables')
for x in mycursor:
    print(x)
'''