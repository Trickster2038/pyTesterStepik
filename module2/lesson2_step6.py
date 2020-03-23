import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element_by_css_selector("#input_value")
	xt = x.text
	#x_element = browser.find_element_by_css_selector("#input_value")
	#x = x_element.text
	y = calc(xt)

	b_element = browser.find_element_by_css_selector("#answer")
	b_element.send_keys(str(y))

	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)

	check = browser.find_element_by_css_selector("#robotCheckbox")
	radio = browser.find_element_by_css_selector("#robotsRule")
	check.click()
	radio.click()

	time.sleep(1)

	button.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()