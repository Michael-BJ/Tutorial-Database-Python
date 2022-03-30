import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '',
    database = 'tutorial3'
)

# cursor = db.cursor()
# show_data = "SELECT * FROM perpus"
# cursor.execute(show_data)


# menampilkan isi dari database menggunakan method fetchall
# results = cursor.fetchall()
# for i in results:
#   print(i)


# menampilkan isi dari database menggunakan method fetchone
# results = cursor.fetchone()
# print(results)

# print("============")
# print("berikut perbedaannya")
# print("============")

# while results is not None:
#   print(results)
#   results = cursor.fetchone()


# Menghapus data di database
# cursor = db.cursor()
# delate = "DELETE FROM perpus WHERE id=%s"
# val = (8, )
# cursor.execute(delate, val)

# print("data berhasil dihapus")
# db.commit()