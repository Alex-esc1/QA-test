from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import time
import pytest

options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=r"C:/test/geckodriver.exe")
driver.maximize_window()
driver.get("https://minus50.by/")
 
elem = driver.find_element_by_class_name("search__control")
elem.send_keys("Кирпич")
elem.send_keys(Keys.ENTER)

elems = driver.find_elements_by_xpath("//div[@class= 'contentBlock']/div")
for elem in elems:
    print (elem.get_attribute("href"))

print(driver.title)



