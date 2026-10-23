from bs4 import BeautifulSoup

def func(number:int):
    if number>=0:
        raise IndexError("Out of the range!")
    else:
        with open(f"Alien-Stage-Data/file_number_{number}.html","r",encoding="utf-8") as file:
            data=file.read()
        return data

def htmlParser(string:str):
    soup=BeautifulSoup(string,"html.parser")
    text=soup.get_text("\u200b \u200b",True)
    link=soup.find_all("a")
    image=soup.find_all("img")
    """if " " in text:
        text=text.replace(" ","-")
    if "  " in text:
        text=text.replace("  ","-")
    if "\n" in text:
        text=text.replace("\n","-")"""
    linkList=[]
    for l in link:
        if "https://accounts.google.com" in l.get("href"):
            pass
        elif "/hashtag" in l.get("href"):
            pass
        elif "https://account.google.com" in l.get("href"):
            pass
        else:
            linkList.append(l.get("href"))
    imagesList=[]
    for i in image:
        if i.get("src")==None:
            pass
        else:
            imagesList.append(i.get("src"))
    return {"text":text,"links":linkList,"images":imagesList}

html=func(-1)
data=htmlParser(html)
yo=data["text"].split("\u200b \u200b")
print(yo[3])
print(len(yo))
#13, the description is of yo[3], the 4th position
