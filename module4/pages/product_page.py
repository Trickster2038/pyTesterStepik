from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def find_code(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        name = self.browser.find_element(*ProductPageLocators.NAME)
        cost = self.browser.find_element(*ProductPageLocators.COST)
        button.click()
        self.solve_quiz_and_get_code()
        cost1 = self.browser.find_element(*ProductPageLocators.COST1)
        name1 = self.browser.find_element(*ProductPageLocators.NAME1)
        #print(cost.text)
        print(cost1.text)
        #print(name.text)
        print(name1.text)
        #assert name.text in name1.text, "Name notification bug"
        #assert cost.text in cost1.text, "Cost notification bug"
