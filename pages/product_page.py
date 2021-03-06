from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        time.sleep(1)
#проверка наличия сообщений
    def check_messages(self):
        messag1 = self.browser.find_element(*ProductPageLocators.MESSAGES1)
        messag2 = self.browser.find_element(*ProductPageLocators.MESSAGES2)
        print('MESSAGES1 -- ',messag1.text,'\nMESSAGES2 -- ',messag2.text)
        assert messag1, 'no message 1'
        assert messag2, 'no message 2'
#сравнение цены из сообщения и из товара
    def price_comparison(self):
        price_1 = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        price_2 = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        print('PRICE1 -- ',price_1,'\nPRICE2 -- ',price_2)
        assert price_1 == price_2, "prices don't match!!!"
#сравнение имени товара в сообщении и в карточке
    def name_comparison(self):
        name_in_mess = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGES).text
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        print('NAME1 -- ',name_in_mess,'\nNAME2 --',name_product)
        assert name_product == name_in_mess, "product don't match!!!"
#is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES1), "Success message is presented, but should not be"
#is_disappeared: будет ждать до тех пор, пока элемент не исчезнет
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGES1), "No Success message is presented"

