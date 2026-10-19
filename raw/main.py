from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

driver=webdriver.Chrome()
driver.get("https://www.youtube.com/@VIVINOS/posts")
time.sleep(240)
#you may ask why am i using sleep here, the reason is, in the 240 seconds, you will have to scroll the posts to extract that, otherwise usually yt will just give the first 10, the rest wouldn't arrive if you don't load it by scrolling 

elem=driver.find_element(By.ID,"contents")
n=0
with open(f"file.html","w",encoding="utf-8") as file:
    file.write(elem.get_attribute("outerHTML"))
time.sleep(60)
driver.close()
#extracting the data...someone tell me how to automate the scrolling of the website :crying: i have to do that manually
