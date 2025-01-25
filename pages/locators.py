from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_TITLE_ADDED = (By.CSS_SELECTOR, "#messages .alertinner strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "#content_inner h1")
    BASKET_COST = (By.CSS_SELECTOR, "#messages .alert-info p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .product_main p")
    BASKET_TOTAL = (By.CSS_SELECTOR, 'div.page_inner div.basket-mini')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert-success')
