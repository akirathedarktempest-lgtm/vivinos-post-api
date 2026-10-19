from bs4 import BeautifulSoup

with open("file.html","r",encoding="utf-8") as file:
    data=file.read()

soup=BeautifulSoup(data,"html.parser")
doc=soup.find_all("ytd-backstage-post-thread-renderer")
print(len(doc))