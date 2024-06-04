from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sqlite3

import time
import sys
import os

currdir = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) != 3:
    print("ERROR: incorrect arguments\nusage: python3 scraper.py https://example.booru.com your_search_term")
    quit() 


firefox_options = Options()
#firefox_options.add_argument("--headless")

site = sys.argv[1] 
driver = webdriver.Firefox(options=firefox_options)
driver.install_addon(os.getcwd() + "/../extensions/ublock_origin-1.58.0.xpi", temporary=True)
driver.get(site)

driver.find_element(By.CSS_SELECTOR, "input").send_keys(sys.argv[2] + Keys.ENTER)
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='content']")))

imgdb= sqlite3.connect("../img.db")
cursor = imgdb.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS imgs(id INTEGER PRIMARY KEY, filename TEXT, link TEXT, tags TEXT, favorite TEXT);")

imgs = [] 

while(True):
    imgs = driver.find_elements(By.CSS_SELECTOR, "img")
    for img in imgs:
        tags = img.get_attribute("title")
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).click(img).key_up(Keys.CONTROL).perform()
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        full_res_img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[id='image']")))
        src = full_res_img.get_attribute("src")
        filename = src.split('/')[-1]
        os.system("curl -o " + currdir + "/../images/" + filename + " "  + src)
        print(filename)
        
        driver.close()
        driver.switch_to.window(handles[0])
        
                

    try:
        driver.find_element(By.CSS_SELECTOR, "a[alt='next']").click()
    except NoSuchElementException:
        break


imgdb.commit()
driver.quit()

