from  selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


url  = "https://www.youtube.com/@CigarettesAfterSex/videos"

driver = webdriver.Chrome()
driver.get(url)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)

    # Wait to load page
    time.sleep(5)
    
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height
    

title  = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
views  = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')
date  = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[2]')

result = [{"title":t.text, "views":v.text, "date":d.text} for t, v, d in zip(title, views, date)]

df = pd.DataFrame(result, columns=['title', 'views', 'date'])
df.index += 1 
df.to_csv('CAS.csv', index_label='SN')

driver.quit()