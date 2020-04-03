import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num', ["895", "896","897","898","899","903","904","905"])
def test_different_pages(browser, num):
    link = f"https://stepik.org/lesson/236{num}/step/1"
    browser.get(link)
    tosend = browser.find_element_by_css_selector("#ember68")
    answer = math.log(int(time.time()))
    tosend.send_keys(str(answer))

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME , "submit-submission"))
    )

    button.click()
    tocheck = browser.find_element_by_css_selector(".smart-hints__hint")
    time.sleep(3)
    assert tocheck.text == "Correct!", tocheck.text