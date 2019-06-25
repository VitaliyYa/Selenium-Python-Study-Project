from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_red_test')

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_FORM_INVALID = (By.CSS_SELECTOR, '#login_form_red_test')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
