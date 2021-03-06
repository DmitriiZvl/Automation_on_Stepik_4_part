from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
#проверка наличия сообщений
    def check_messages(self):
        message_checkout = self.is_not_element_present(*BasketPageLocators.CHECKOUT)
        message_basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        print('MESSAGE no checkout -- ',message_checkout)
        print('MESSAGE empty -- ',message_basket_empty)
        assert message_basket_empty == 'Your basket is empty. Continue shopping', 'Products in the basket'
        assert message_checkout, 'No product in cart'
        
        #content_inner
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_EMPTY), "No Success message is presented"
        #assert self.is_disappeared(*BasketPageLocators.CHECKOUT), "No Success message is presented"
