from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_red_test')

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_FORM_INVALID = (By.CSS_SELECTOR, '#login_form_red_test')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators(object):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_TITLE = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class,"product_main")]/p[@class="price_color"]')
    PRODUCT_AVAILABILITY = (By.XPATH, '//div[contains(@class,"product_main")]/p/i[@class="icon-ok"]')
    TOTAL_AMOUNT = (By.XPATH, '//div[contains(@class,"alert-info")]/div[contains(@class,"alertinner")]/p/strong')
    PRODUCT_SUCCESSFULLY_ADDED_TO_BASKET = (By.XPATH, '//div[contains(@class,"alert-success")]/div[contains(@class,"alertinner")]/strong')
