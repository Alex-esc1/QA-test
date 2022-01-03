from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:/test/chromedriver.exe')
driver.get("https://minus50.by/")
input_username = driver.find_element_by_id("user-name")
if input_username is None:
   print("Элемент не найден")
else:
   print("Элемент найден")


