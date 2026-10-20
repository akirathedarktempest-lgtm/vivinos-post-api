from bs4 import BeautifulSoup

def readFunction(number:int):
    with open(f"directory-of-alnst-webscraping/file-{number}.html","r",encoding="utf-8") as file:
        info=file.read()
    return info

soup=BeautifulSoup(readFunction(0),"html.parser")

if soup.find_all("ytd-backstage-image-renderer") is False:
    pass
else:
    print(soup.find_all("ytd-backstage-image-renderer"))
    print(len(soup.find_all("ytd-backstage-image-renderer")))
if soup.find_all("yt-formatted-string") is False:
    pass
else:
    print(soup.find_all("yt-formatted-string"))
    print(len(soup.find_all("yt-formatted-string")))
if soup.find_all("img") is False:
    pass
else:
    print(soup.find_all("img"))
    print(len(soup.find_all("img")))