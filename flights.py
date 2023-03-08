from  selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


url = "https://www.skyscanner.co.in/transport/flights/ktm/del/230312/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&is_banana_refferal=true&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=0"


# Create an options object
# options = Options()

# Set the path to the user data directory
# options.add_argument(r"--user-data-dir=C:\Users\Dell-pc\AppData\Local\Google\Chrome\User Data\new")

# Set the path to the profile directory
# options.add_argument(r"--profile-directory=Arun Mahara")
# options.add_argument("C:\Users\Dell-pc\AppData\Local\Google\Chrome\User Data\Default")
driver = webdriver.Firefox()
time.sleep(2)
driver.get(url)
time.sleep(20)


# element = driver.find_element(By.XPATH, '//*[@id="SadJMUvBiTOwztY"]')
# action = ActionChains(driver)
# click = ActionChains(driver)
# action.click_and_hold(element)
# action.perform()
# time.sleep(10)
# action.release(element)
# action.perform()
# time.sleep(0.2)
# action.release(element)

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
    
flights = driver.find_elements(By.CLASS_NAME, 'FlightsTicket_container__NWJkY')
print(flights)
for each in flights:
    # airlines = each.find_element(By.XPATH, '//*[@id="app-root"]/div[1]/div/div/div/div[1]/div[3]/div[3]/div/div[3]/a/div/div[1]/div/div/div[1]/div/span').text
    airlines = each.find_element(By.CLASS_NAME, 'BpkText_bpk-text__ZWIzZ.BpkText_bpk-text--xs__MTAxY').text
    print(airlines)

driver.quit()