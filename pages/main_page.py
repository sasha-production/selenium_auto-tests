from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        ## Первый способ: возвращать нужный Page Object
        # return LoginPage(browser=self.browser, url=self.browser.current_url)  # явно возвращаем страницу
        ## Второй подход: переход происходит неявно, страницу инициализируем в теле теста:

        # alert = self.browser.switch_to.alert # если на странице есть alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
