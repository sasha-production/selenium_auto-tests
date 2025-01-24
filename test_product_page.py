from pages.product_page import ProductPage


def test_guest_should_add_product_to_basket(browser):
    # link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link2)
    page.open()
    page.should_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_title_and_price_after_adding_to_basket()

