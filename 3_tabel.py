import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "M_Andra_A"
)

cursor = mydb.cursor()
sql1 = """Create Table movie(tahun Varchar(10) Primary Key, judul Varchar(50), genre Varchar(20), studio Varchar(20))"""
sql2 = """Create Table baju(ukuran Varchar(10) Primary Key, tinggi Varchar(30), lebar Varchar(20), dada Varchar(20))"""

cursor.execute(sql1)
cursor.execute(sql2)

print("Tabel berhasil dibuat")