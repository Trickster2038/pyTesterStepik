from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	NAME = (By.CSS_SELECTOR, ".product_main h1")
	COST = (By.CSS_SELECTOR, ".product_main .price_color")
	NAME1 = (By.CSS_SELECTOR, ".alert-success")
	COST1 = (By.CSS_SELECTOR, ".alert-info")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")