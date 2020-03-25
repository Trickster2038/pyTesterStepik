from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element_by_css_selector(".trollface")
    btn1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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

    btn2 = browser.find_element_by_css_selector(".btn-primary")
    btn2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()