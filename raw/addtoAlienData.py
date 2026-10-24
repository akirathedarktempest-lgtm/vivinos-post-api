import csv
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3

connect=sqlite3.connect("Alien-Stage.db")
cursor=connect.cursor()

with open("Alien-Stage-Data/.csv","r") as file:
    read=csv.reader(file)
    for r in read:
        number=int(r[0])
    number-=1

with open("raw-files/raw-file-1.html","r",encoding="utf-8") as f:
    data=f.read()

soup=BeautifulSoup(data,"html.parser")
info=soup.find_all("ytd-backstage-post-renderer")
alnst=str(info[0])

with open(f"Alien-Stage-Data/file_number_{number}.html","w",encoding="utf-8") as alien:
    alien.write(alnst)

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

html=htmlParser(alnst,number)
print(html)

cursor.execute("INSERT INTO vivinosYTPost VALUES (?,?,?,?,?,?,?,?,?,?)",[html["number"],html["title"],html["authorLink"],html["authorImage"],html["postLink"],html["links"],
                                                                             html["images"],html["hashtags"],html["description"],html["updated"]])
connect.commit()
connect.commit()