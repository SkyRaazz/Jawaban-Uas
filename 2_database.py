import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

cursor = mydb.cursor()
cursor.execute("Create Database M_Andra_A")

print("Database berhasil dibuat")