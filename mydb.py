import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'rootroot'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE prisonmike")

print("Task completed!")