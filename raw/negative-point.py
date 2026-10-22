from pathlib import Path
import time

n=-1

folder=Path("Alien-Stage-Data")
folder.mkdir(parents=True,exist_ok=True)

def Call():
    global n
    for i in range(199,-1,-1):
        print(i)
        with open(f"directory-of-alnst-webscraping/file-{i}.html","r",encoding="utf-8") as file:
            data=file.read()
        with open(f"Alien-Stage-Data/file_number_{n}.html","w",encoding="utf-8") as f:
            f.write(data)
        print(f"file {n} created!")
        n-=1
        time.sleep(1)
Call()
#replacing the files from positive number to negative, why?
#because if we stay at positive and tomorrow is Friday (today is 10-22-2026 Thursaday) so there will be a new update, and in case of positive
#the file 0 should become 1, file 1 will become 2 and everyone will be affected by one number changing
#but, in case of negative, we will just add the new ones with the new number, -1 will be the last and will not be affected, and there will be just a new number
#and i kept from 199 to -1 because there are just 200 i got, i don't know if it's all or not but yeah...and all set!