#spliting each part into small to make it easier
from bs4 import BeautifulSoup
from pathlib import Path
import time

with open("file.html","r",encoding="utf-8") as file:
    data=file.read()

soup=BeautifulSoup(data,"html.parser")
doc=soup.find_all("ytd-backstage-post-renderer")

folder=Path("directory-of-alnst-webscraping")
folder.mkdir(parents=True,exist_ok=True)#makes a folder
n=0
for i in doc:
    with open(f"directory-of-alnst-webscraping/file-{n}.html","w",encoding="utf-8") as file:
        file.write(str(i))
    print(f"file {n} created")
    time.sleep(1)#sleep because scared if crashes, so let it happen slowly slowly
    n+=1
