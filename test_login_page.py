from pages.login_page import LoginPage


def test_guest_should_be_on_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
