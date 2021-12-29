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
'''mycursor.execute('show tables')
for x in mycursor:
    print(x)'''

mycursor.execute('INSERT INTO `pythonprgm`.`customers`(`name`, `address`) VALUES ("Ram", "HYD");')
'''
mycursor.execute('select * from `pythonprgm`.`customers` LIMIT 10')
for i in mycursor:
    print(i)
'''