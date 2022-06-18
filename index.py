import time
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from bsActions import *

url = 'https://www.aliexpress.com/'

driver = webdriver.Firefox()
actions = ActionChains(driver)

driver.get(url)
driver.fullscreen_window()
time.sleep(1)

close_button = driver.find_element(By.CLASS_NAME, 'btn-close')
driver.execute_script("arguments[0].click();", close_button)

menu_items = driver.find_elements(By.CLASS_NAME, 'cl-item')
data = []

for item in menu_items:
    actions.move_to_element(item).perform()
    time.sleep(1)
    source = item.get_attribute('innerHTML')
    heading = item.find_element(By.XPATH, './dt/span/a').text
    secondary_cate = extract_data(heading, source)

    data.append(secondary_cate)

driver.close()

with open('categories2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
