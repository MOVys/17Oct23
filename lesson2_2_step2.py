from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import math


# Открыть страницу https://suninjuly.github.io/selects1.html
link = "https://suninjuly.github.io/selects2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

# Считать num1 и num2
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    print("Num1 равно=", num1)
    print("Num2 равно=", num2)

# Посчитать сумму заданных чисел
    summ = num1 + num2
    print("сумма этих чисел:", summ)

# Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ)) # ищем элемент с текстом "Python"

# Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

# select = Select(browser.find_element(By.TAG_NAME, "select"))
# select.select_by_value("1") # ищем элемент с текстом "Python"
# Можно использовать еще два метода: 

# select.select_by_visible_text("text") 
# и select.select_by_index(index). 
# Первый способ ищет элемент по видимому тексту, например, 
# select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

# Второй способ ищет элемент по его индексу или порядковому номеру.
# Индексация начинается с нуля. 
# Для того чтобы найти элемент с текстом "Python", нужно использовать 
# select.select_by_index(1), 
# так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".


