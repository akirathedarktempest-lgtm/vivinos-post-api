import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

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
            continue
        elif "/@VIVINOS" in l.get("href"):
            authorLink=f"https://youtube.com{l.get("href")}"
        elif "/post/" in l.get("href"):
            postLink=f"https://youtube.com{l.get("href")}"
        else:
            link+=f"{l.get("href")}\u200b-\u200b"
    for i in images:
        if i.get("src")==None:
            continue
        if i.get("src").startswith("//"):
            authorImage=""
            for z in range(len(i.get("src"))):
                if z==0 or z==1:
                    pass
                else:
                    authorImage+=i.get("src")[z]
        else:
            img+=f"{i.get("src")}\u200b-\u200b"
    return {"images":img,"authorLink":authorLink,"authorImage":authorImage,"number":number,"description":letter,"postLink":postLink,"title":title,"datetime":f"{datetime.now()} +05:30"}

data=func(-1)
information=htmlParser(data[0],data[1])
print(information)

connect.close()