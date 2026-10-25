import sqlite3

def pushPost(number):
    if number>=0:
        number=number-lengthPost()
    connect=sqlite3.connect("Alien-Stage.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM vivinosYTPost WHERE id=?",[number])
    data=cursor.fetchall()
    data=data[0]
    connect.close()
    return data

def lengthPost():
    connect=sqlite3.connect("Alien-Stage.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM vivinosYTPost ORDER BY id ASC")
    data=cursor.fetchall()
    connect.close()
    return len(data)

data=pushPost(1)
print(data)