#from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#path to webdriver
driver = webdriver.Chrome()

driver.implicitly_wait(5)


driver.get('https://www.amazon.com/')
searchbox = driver.find_element(By.ID,'twotabsearchtextbox')
searchbox.send_keys('dress',Keys.ENTER)

expected_text= '"dress"'
actual_text =driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold']").text
assert expected_text == actual_text, f'Error. Expected text: {expected_text}, but actual text:{actual_text}'
driver.quit()
