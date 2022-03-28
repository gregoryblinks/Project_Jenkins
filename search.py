from re import search
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FlaskblogHomePage:
    URL = 'http://127.0.0.1:5000/home'

    SEARCH_INPUT = (By.NAME, 'Jenkins')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.Return)