import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

def  test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = ProductPage(browser, link)
	page.open()  
	page.find_code()

