from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import math


# Открыть страницу https://SunInJuly.github.io/execute_script.html.
link = "https://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)


# Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print("Значение x равно", x)

# Посчитать математическую функцию от x.
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
        
# Проскроллить страницу вниз.

    answer = browser.find_element(By.ID, "answer")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

# Переключить radiobutton "Robots rule!".
    option2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
# Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()