from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url_page = self.browser.current_url
        assert '/accounts/login/' in url_page, f"{url_page} is not login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "there is no login form on page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        register_form = self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "there is no register form on page"
