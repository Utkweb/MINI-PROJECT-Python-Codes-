import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user ="root",
    passowrd= "",
    database="bank"
)

if mydb.is_connected():
    print("My database is connected")
else:
    print("my databse is not connected")
