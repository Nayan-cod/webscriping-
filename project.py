from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
qury="leptop"
file=0

for i in range(1,20):

    driver.get(f"https://www.amazon.in/s?k={qury}&page={i}&crid=2U44J85V9C94J&qid=1730569759&sprefix=lep%2Caps%2C757&ref=sr_pg_2")
    elems=driver.find_elements(By.CLASS_NAME,"puis-card-container")
    print(f"{len(elems)} items found")

    for elem in elems:
       d=elem.get_attribute("outerHTML")
       with open(f"data2/{qury}_{file}.html","w",encoding="utf-8") as f:
           f.write(d)
           file+=1
   
driver.close()