from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import time

#Открыть страницу http://suninjuly.github.io/get_attribute.html.
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()
    