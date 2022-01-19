import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'tutorial 2'
)


cursor = db.cursor()
cursor.execute(
    """
    CREATE TABLE perpus3(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    buku VARCHAR(100) NOT NULL
    )
    """
)

print("Table berhasil dibuat")