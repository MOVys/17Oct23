from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"  # Или новая ссылка

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
    first_name.send_keys("Test")

    last_name = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
    last_name.send_keys("Alsodev")

    email = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
    email.send_keys("test@gmail.com")

    # Остальные поля и действия на странице

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверка успешной регистрации
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

except NoSuchElementException:
    print("Элемент не найден на странице. Вероятно, страница была изменена.")

finally:
    time.sleep(5)
    browser.quit()