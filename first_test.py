from selenium import webdriver
 
driver = webdriver.Firefox(executable_path=r"C:/test/geckodriver.exe")
driver.get('http://minus50.by/')
# Разворачиваем окно, нам ведь еще скрины делать
driver.maximize_window()
driver.find_element_by_class_name('search__btn')

# Делаем скриншот результата
driver.save_screenshot('1.png')
 
driver.close()