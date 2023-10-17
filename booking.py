from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


#Открыть страницу http://suninjuly.github.io/explicit_wait2.html.
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

# считать х
    x_element = browser.find_element(By.ID, "input_value")
    x =  x_element.text
    print("Х равно = ", x)

# считаемая функция
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
# Ввести ответ в текстовое поле.
    y = calc(x)
    print("Значение y равно", y)
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)      

# Нажать на кнопку Submit.

    button2 = browser.find_element(By.ID, "solve")
    button2.click()
    
    
finally:
    time.sleep(5)
    browser.quit()
    

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 
# (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить задачу
# Чтобы определить момент, когда цена аренды уменьшится до $100, 
# используйте метод text_to_be_present_in_element из библиотеки expected_conditions.