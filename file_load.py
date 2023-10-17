from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import math
import os 

# Открыть страницу http://suninjuly.github.io/file_input.html
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

# Заполнить текстовые поля: имя, фамилия, email
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Marina")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Vysotskaya")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("vippmar@gmail.com")

# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    loadfile = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file_load.txt')           # добавляем к этому пути имя файла 
    loadfile.send_keys(file_path)


# Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# print("current_dir ===",current_dir)
# print("file_path ===", file_path)

finally:
    time.sleep(5)
    browser.quit()
    