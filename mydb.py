import mysql.connector

dateBase = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=""
)

cursorObject = dateBase.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS elhadrami119")

print("Database created successfully!")