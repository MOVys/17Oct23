from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import time
import math

# Открыть страницу http://suninjuly.github.io/redirect_accept.html.
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

# Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

# Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
# Пройти капчу для робота и получить число-ответ    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print("Х равно = ", x)
    
# Посчитать математическую функцию от x (код для этого приведён ниже).
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    y = calc(x)
    print("У равно = ", y)
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button2.click()
    
    

    
finally:
    time.sleep(5)
    browser.quit()
    
    





# browser.switch_to.window(window_name)
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, 
# который возвращает массив имён всех вкладок. Зная, что в браузере теперь 
# открыто две вкладки, выбираем вторую вкладку:

# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

# first_window = browser.window_handles[0]
