import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "M_Andra_A"
)

cursor = mydb.cursor()
sql1 = "Insert Into movie (tahun, judul, genre, studio) Values (%s, %s, %s, %s)"
val1 = [("2020", "Peninsula", "Horror", "redpeter"), ("2021", "Spider Man : No Way Home", "Action", "Marvel"), ("2022", "Uncharted", "Adventure", "Columbia Pictures"), ("2023", "Transformers: Rise of the Beast", "Sci-Fi", "Paramount Pictures")]


sql2 = "Insert Into baju (ukuran, tinggi, lebar, dada) Values (%s, %s, %s, %s)"
val2 = [("M", "70cm", "49cm", "99cm"), ("L", "72cm", "52cm", "105cm"), ("xl", "75cm", "55cm", "111cm"), ("XXL", "77cm", "58cm", "117cm")]

for x in val1:
    cursor.execute(sql1, x)
    
for x in val2:
    cursor.execute(sql2, x)

mydb.commit()
print("Data berhasil ditambahkan")