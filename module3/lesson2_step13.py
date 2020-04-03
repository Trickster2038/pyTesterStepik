from selenium import webdriver
import time
import unittest

class TestReg(unittest.TestCase):
    def test_t1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("qwerty")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("qwerty")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("qwerty")
        input4 = browser.find_element_by_css_selector(".second_block .first")
        input4.send_keys("qwerty")
        input5 = browser.find_element_by_css_selector(".second_block .second")
        input5.send_keys("qwerty")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 
            "Should be welcome message")
    def test_t2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("qwerty")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("qwerty")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("qwerty")
        input4 = browser.find_element_by_css_selector(".second_block .first")
        input4.send_keys("qwerty")
        input5 = browser.find_element_by_css_selector(".second_block .second")
        input5.send_keys("qwerty")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 
            "Should be welcome message")

if __name__ == "__main__":
    unittest.main()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()