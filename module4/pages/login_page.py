from .base_page import BasePage
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        x = self.browser.current_url();
        assert "login" in x, "Not a login link"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # x = login_link = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert self.browser.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.is_element_present(*LoginPageLocators.REGISTER_FORM)