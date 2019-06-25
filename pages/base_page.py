from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.firefox.webdriver import WebDriver


class BasePage (object):
    def __init__(self, browser, url, timeout = 10):
        # self.browser = browser
        self.browser: WebDriver = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
