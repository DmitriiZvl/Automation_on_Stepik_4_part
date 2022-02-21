from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        time.sleep(1)

    def check_messages(self):
        messag1 = self.browser.find_element(*ProductPageLocators.MESSAGES1)
        messag2 = self.browser.find_element(*ProductPageLocators.MESSAGES2)
        print('MESSAGES1 -- ',messag1.text,'\nMESSAGES2 -- ',messag2.text)
        assert messag1, 'no message 1'
        assert messag2, 'no message 2'

    def price_comparison(self):
        price_1 = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        price_2 = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        print('PRICE1 -- ',price_1,'\nPRICE2 -- ',price_2)
        assert price_1 == price_2, "prices don't match!!!"

    def name_comparison(self):
        messag1 = self.browser.find_element(*ProductPageLocators.MESSAGES1).text
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        print('NAME1 -- ',messag1,'\nNAME2 --',name_product)
        assert name_product in messag1, "product don't match!!!"


