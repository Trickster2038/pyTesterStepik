from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.webdriver.chrome.options import Options
import time
from selenium.common import exceptions 

class ProductPage(BasePage):
    def find_code(self):
        self.browser.implicitly_wait(10)
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        name = self.browser.find_element(*ProductPageLocators.NAME)
        cost = self.browser.find_element(*ProductPageLocators.COST)
        namet = name.text
        costt = cost.text
        print("<name>")
        print(namet)
        print("</name>")
        print(costt)
        button.click()
        self.solve_quiz_and_get_code()
        cost1 = self.browser.find_element(*ProductPageLocators.COST1)
        name1 = self.browser.find_element(*ProductPageLocators.NAME1)
        print("<name1>")
        print(name1.text)
        print("</name1>")
        print(cost1.text)
        #print(cost.text)
        
        
        assert f"{namet} был добавлен в вашу корзину." in name1.text, "Name notification bug"
        assert costt in cost1.text, "Cost notification bug"
    
    def no_msg_after(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def no_msg(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def no_msg_after_time(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        time.sleep(1)
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"