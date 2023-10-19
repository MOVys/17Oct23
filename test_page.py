from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()
required_fields = ['.first_block .first_class input',
                   '.first_block .second_class input',
                   '.first_block .third_class input']
expected_message = "Congratulations! You have successfully registered!"

# Создать класс, который должен наследоваться от класса TestCase: 
# class TestAbs(unittest.TestCase):
class TestPage(unittest.TestCase):
    def test_page_positive(self):
        link_positive = "http://suninjuly.github.io/registration1.html"
        browser.get(link_positive)

        input1 = browser.find_element("xpath", "//input[contains(@class, 'first') and @required]")
        input1.send_keys("Marina")
        input2 = browser.find_element("xpath", "//input[contains(@class, 'second') and @required]")
        input2.send_keys("Vysotskaya")
        input3 = browser.find_element("xpath", "//input[contains(@class, 'third') and @required]")
        input3.send_keys("email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "текст не сопадает")

        #self.assertEqual(expected_message, welcome_text,
        #                 f'Text "{welcome_text}" matches with expected_message: {expected_message}')

    def test_page_negative(self):
        link_negative = "http://suninjuly.github.io/registration2.html"
        browser.get(link_negative)

        input1 = browser.find_element("xpath", "//input[contains(@class, 'first') and @required]")
        input1.send_keys("Marina")
        input2 = browser.find_element("xpath", "//input[contains(@class, 'second') and @required]")
        input2.send_keys("Vysotskaya")
        input3 = browser.find_element("xpath", "//input[contains(@class, 'third') and @required]")
        input3.send_keys("email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "текст не сопадает")

        #self.assertEqual(expected_message, welcome_text,
        #                 f'Text "{welcome_text}" matches with expected_message: {expected_message}')

# Заменить строку запуска программы на unittest.main()
if __name__ == "__main__":
    unittest.main()