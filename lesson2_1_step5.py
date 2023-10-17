from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import time
import math

# Открыть страницу https://suninjuly.github.io/math.html.
link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
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
# Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

# Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
# Нажать на кнопку Submit.

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
    
   # body > div > form > button