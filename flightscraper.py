from selenium import webdriver
import facebook
import urllib3
import requests
#driver = webdriver.Chrome()
token  = 'EAAEGxrS0wZAsBAH7A5YVSuN4yaJyem0uoKHuD8oZAV9QGDyJV7h7lZBS2NwscrcC2Aj6LLf566UrzGmBn2e3nZCho7MMknN71A1N5PFFZAukxlLMaI4hhyqeYjkrIc3xEwCa3frv2DQdvwdTqI7ZAa0WlGmumt2dB45L7w2q6sJjmiZAGNpNq550HEvP0eGcFZBiT1Jdivw6au4ZCIhFoxA5A'
driver.set_window_size(1024, 768)
graph = facebook.GraphAPI(access_token="your_token", version="2.12")


element = driver.find_element_by_name('q')
element.send_keys(token) 
#btnK
element.submit()