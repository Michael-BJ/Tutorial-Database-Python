import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'tutorial1'
)

# cara membuat database
# cursor = db.cursor()
# cursor.execute("CREATE DATABASE tutorial1")

# print("database berhasil dibuat")

if db.is_connected():
    print("berhasil")