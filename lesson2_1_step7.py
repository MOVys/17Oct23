from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import time
import math

#Открыть страницу http://suninjuly.github.io/get_attribute.html.
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    x_picture = browser.find_element(By.ID, "treasure")

# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = x_picture.get_attribute("valuex")
    print("Значение элемента: ", x)
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
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
# Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    		
finally:
    time.sleep(5)
    browser.quit()
    
    