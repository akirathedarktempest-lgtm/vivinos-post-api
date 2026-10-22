from bs4 import BeautifulSoup

with open("directory-of-alnst-webscraping/file-20.html","r",encoding="utf-8") as file:
    html=file.read()

soup=BeautifulSoup(html,"html.parser")
images=soup.find_all("img")
text=soup.text
links=soup.find_all("a")
for i in images:
    print(i.get("src"))
if "\n\n" in text:
    text=text.replace("\n\n",'\n')
if "\n" in text:
    text=text.replace("\n","-")
data=text.split("-")
l=[]
if "" in data:
    for z in data:
        if z=="" or z==" " or z=="  ":
            continue
        else:
            l.append(z)
print(text)
print(l)
for n in links:
    if "https://account.google.com" in n.get("href"):
        continue
    if "/hashtag" in n.get("href"):
        continue
    if "https://accounts.google.com" in n.get("href"):
        continue
    print(n.get("href"))
print(len(links))
