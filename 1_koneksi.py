import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

if mydb.is_connected():
    print("Database berhasil terhubung")