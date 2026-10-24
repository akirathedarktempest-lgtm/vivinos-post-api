import sqlite3

connect=sqlite3.connect("Alien-Stage.db")
cursor=connect.cursor()

cursor.execute("SELECT * FROM vivinosYTPost WHERE id=?",[-1])
data=cursor.fetchall()
print(f"{data}\n{data[0]}")

connect.close()