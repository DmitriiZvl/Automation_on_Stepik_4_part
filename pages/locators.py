from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET = (By.CSS_SELECTOR,'#add_to_basket_form > button')
    
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
