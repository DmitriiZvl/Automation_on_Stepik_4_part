from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')

class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR,'#add_to_basket_form > button')
    MESSAGES1 = (By.CSS_SELECTOR,'#messages > div:nth-child(1)')
    MESSAGES2 = (By.CSS_SELECTOR,'#messages > div:nth-child(2)')
    PRICE_IN_CART = (By.CSS_SELECTOR,'#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR,'#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    NAME_PRODUCT = (By.CSS_SELECTOR,'#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    NAME_IN_MESSAGES = (By.CSS_SELECTOR,'#messages > div:nth-child(1) > div > strong')
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators():
#enter
    EMAIL_ADDRESS_IN= (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_IN= (By.CSS_SELECTOR, "id_login-password.form-control")
    LOGIN_SUBMIT_IN= (By.NAME, "login_submit")
    
#registration
    EMAIL_ADDRESS_REG= (By.CSS_SELECTOR, "#login_submit")
    PASSWORD_REG_1= (By.NAME, "registration-password1")
    PASSWORD_REG_2= (By.NAME, "registration-password2")
    LOGIN_SUBMIT_REG= (By.NAME, "registration_submit")

class BasketPageLocators():
    CHECKOUT = (By.CSS_SELECTOR, '#content_inner > div.form-group.clearfix > div > div > a')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')