from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    btn1 = browser.find_element_by_css_selector("#book")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    btn1.click()

    xv = browser.find_element_by_css_selector("#input_value")
    x = xv.text
    print(x)
    x = int(x)
    # не забывать str -> int -> str
    y = math.log(abs(12*(math.sin(x))))
    print(y)
    target = browser.find_element_by_css_selector("#answer")
    target.send_keys(str(y))
    # ждем загрузки страницы
    time.sleep(1)

    btn2 = browser.find_element_by_css_selector("#solve")
    btn2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()