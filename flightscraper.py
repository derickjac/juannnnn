from selenium import webdriver
import facebook
driver = webdriver.Chrome()

driver.set_window_size(1024, 768)

driver.get("https://google.com")

element = driver.find_element_by_name('q')
element.send_keys('testing') 
#btnK
element.submit()