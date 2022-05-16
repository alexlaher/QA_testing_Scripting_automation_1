from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service('D:\PyCharm\chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)

driver.get('https://www.amazon.com/')

search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('dress', Keys.ENTER)

expected_text  = '"dress"'
actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_text == actual_text, f'Error, Expected text {expected_text}, but actual text {actual_text}'


driver.quit()