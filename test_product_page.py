
from .pages.product_page import ProductPage
import time 
from selenium.webdriver.common.by import By

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    
    page.check_messages()
    page.price_comparison()
    page.name_comparison()
    
    
    
    

#messages > div:nth-child(1)
#messages > div:nth-child(2)
#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong
#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color