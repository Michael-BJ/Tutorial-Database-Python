import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'tutorial3'
)


cursor = db.cursor()
query = "INSERT INTO perpus1(nama, email, buku) VALUES(%s, %s, %s)"
data = ("budi", "et", "Belajar database")

cursor.execute(query, data)

db.commit()
print("Data berhasil di insert")