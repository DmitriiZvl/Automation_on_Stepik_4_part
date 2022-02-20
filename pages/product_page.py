from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
import time

class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        link.click()
        time.sleep(1)
       


