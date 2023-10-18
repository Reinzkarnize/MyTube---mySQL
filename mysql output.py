import mysql.connector

conn = mysql.connector.connect(host='localhost', password='a4867787', user='root', database="mytube")

db = conn.cursor()

db.execute("SELECT * FROM users")

rows = db.fetchall()

print(rows)
