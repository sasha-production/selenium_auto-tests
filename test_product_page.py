import time

import pytest

from pages.product_page import ProductPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                      marks=pytest.mark.xfail),
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.skip(reason='ran in prev step')
@pytest.mark.parametrize('link', links)
def test_guest_should_add_product_to_basket(browser, link):
    # link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.current_basket_total()  #
    page.should_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_title_and_price_after_adding_to_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()
    page.should_be_no_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_no_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
