import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime
import time

connect=sqlite3.connect("Alien-Stage.db")
cursor=connect.cursor()

def func(number:int):
    with open(f"Alien-Stage-Data/file_number_{number}.html","r",encoding="utf-8") as file:
        data=file.read()
    return [data,number]

def htmlParser(data:str,number:int):
    soup=BeautifulSoup(data,"html.parser")
    links=soup.find_all("a")
    text=soup.get_text("\u200b \u200b",True)
    images=soup.find_all("img")
    textL=text.split('\u200b \u200b')
    title=textL[0]
    hashTag=""
    if len(textL)<=12:
        letter='none'
    else:
        letter=textL[3]
    img=""
    link=''
    for l in links:
        if "https://accounts.google.com" in l.get("href"):
            continue
        elif "/hashtag" in l.get("href"):
            hashTag+=f"https://www.youtube.com{l.get("href")}\u200b-\u200b"
        elif "/@VIVINOS" in l.get("href"):
            authorLink=f"https://youtube.com{l.get("href")}"
        elif "/post/" in l.get("href"):
            postLink=f"https://youtube.com{l.get("href")}"
        else:
            link+=f"{l.get("href")}\u200b-\u200b"
    if link=='':
        link='none'
    if hashTag=='':
        hashTag='none'
    for i in images:
        if i.get("src")==None:
            continue
        if i.get("src").startswith("//"):
            authorImage=f"https:{i.get("src")}"
        else:
            img+=f"{i.get("src")}\u200b-\u200b"
    return {"hashtags":hashTag,"links":link,"images":img,"authorLink":authorLink,"authorImage":authorImage,"number":number,"description":letter,"postLink":postLink,"title":title,"updated":f"{datetime.now()} +05:30"}

"""data=func(-1)
information=htmlParser(data[0],data[1])
print(information)"""

cursor.execute("""CREATE TABLE vivinosYTPost(
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    authorLink TEXT,
                    authorImage TEXT,
                    postLink TEXT,
                    links TEXT,
                    images TEXT,
                    hashtagLinks TEXT,
                    description TEXT,
                    updated_last_time TEXT)""")

for i in range(-1,-201,-1):
    data=func(i)
    html=htmlParser(data[0],data[1])
    if data[1]==i:
        pass
    else:
        raise "Wrong!!!"
    cursor.execute("INSERT INTO vivinosYTPost VALUES (?,?,?,?,?,?,?,?,?,?)",[html["number"],html["title"],html["authorLink"],html["authorImage"],html["postLink"],html["links"],
                                                                             html["images"],html["hashtags"],html["description"],html["updated"]])
    connect.commit()
    time.sleep(1)
    print(f"done {html['number']}...maybe...")

connect.close()
#adding database, and here you can find the database, .db somewhere, i would have uploaded it, but the latest one is not updated :(
