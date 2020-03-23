import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x1e = browser.find_element_by_css_selector("#num1")
	x1 = x1e.text
	x2e = browser.find_element_by_css_selector("#num2")
	x2 = x2e.text


	y = int(x1) + int(x2)


	print(x1,x2,y, str(y))

	elem = Select(browser.find_element_by_css_selector("#dropdown"))
	elem.select_by_value(str(y))

	time.sleep(1)

	button = browser.find_element_by_css_selector("""[text()="Submit"]""")
    #button.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()