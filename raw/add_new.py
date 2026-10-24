from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver=webdriver.Chrome()
driver.get("https://www.youtube.com/@VIVINOS/posts")
time.sleep(60)

elem=driver.find_element(By.ID,"contents")

with open("raw-files/.csv","r",newline='') as file:
    reader=csv.reader(file)
    for r in reader:
        number=int(r[0])+1

with open("raw-files/.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow([number])

with open(f"raw-files/raw-file-{number}.html","w",encoding="utf-8") as html:
    html.write(elem.get_attribute("outerHTML"))

driver.close()