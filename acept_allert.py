from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import time
import math

# Открыть страницу http://suninjuly.github.io/alert_accept.html
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

# Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    
# Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print("Значение x равно", x)
    
# Посчитать математическую функцию от x (код для этого приведён ниже).
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
# Ввести ответ в текстовое поле.
    y = calc(x)
    print("Значение y равно", y)
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)
    
# Нажать на кнопку Submit.
    button2 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button2.click()

    
finally:
    time.sleep(5)
    browser.quit()
    