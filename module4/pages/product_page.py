from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def find_code(self):
		button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
		button.click()
		self.solve_quiz_and_get_code()
