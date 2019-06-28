import math

from .locators import BasePageLocators

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def go_to_login_page(self):
        """Метод переход на страницу ввода логина"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        """Метод переход на страницу корзины"""
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def open(self):
        """Метод перехода по ссылке"""
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        """Проверка: пользователь залогинен"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'User icon is not presented,' \
                                                                     ' probably unauthorised user'

    def should_be_login_link(self):
        """Метод проверки ссылки для входа"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def solve_quiz_and_get_code(self):
        """метод для получения проверочного кода"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f'Your code: {alert.text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')
