from fastapi import FastAPI,HTTPException
import sqlite3

app=FastAPI()

def pushPost(number):
    if number>=0:
        number=number-lengthPost()
    else:
        pass
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

@app.get("/vivinos/yt/post/{number}")
def getPost(number:int):
    if number<0:
        number=number+lengthPost()
    else:
        pass
    if number>=0:
        if lengthPost()<=number:
            raise HTTPException(404)
        else:
            data=pushPost(number)
            title=data[1]
            authorLink=data[2]
            authorImage=data[3]
            postLink=data[4]
            link=data[5]
            links=[]
            if link=='none':
                links=[None]
            else:
                l=link.split("\u200b-\u200b")
                for li in l:
                    if li=='':
                        continue
                    links.append(li)
            img=data[6]
            images=[]
            if img=="none":
                images=[None]
            else:
                image=img.split("\u200b-\u200b")
                for i in image:
                    if i=='':
                        continue
                    images.append(i)
            hashtag=data[7]
            tags=[]
            if hashtag=="none":
                tags=[None]
            else:
                tag=hashtag.split("\u200b-\u200b")
                for t in tag:
                    if t=='':
                        continue
                    tags.append(t)
            desc=data[8]
            updated=data[9]
            return {"authorName":title,"authorLink":authorLink,"authorImage":authorImage,"postLink":postLink,"links":links,"images":images,"hashtag":tags,"description":desc,"last_time_updated":updated}
    else:
        raise HTTPException(404)
