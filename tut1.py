
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from main import *

#https://github.com/mozilla/geckodriver/releases



browser.get("https://lsbuuniversity.powerhousehub.net/")
time.sleep(3)

#user= browser.find_element_by_name("username")
#element =browser.find_element(By.ID, ‘username’)
element =browser.find_element(By.NAME, "username")
#element = browser.find_element_by_id("username")

element_2 = browser.find_element(By.ID,"password")
#pwd = browser.find_element_by_name("password")

element.send_keys("test")
element_2.send_keys("test")
element_2.send_keys(Keys.RETURN)
time.sleep(3)
#pwd.send_keys("test")

