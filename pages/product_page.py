import re

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    basket_total: float

    def product_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        return product_title

    def product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip().replace('£', '')
        return float(product_price)

    def current_basket_total(self):
        basket_total_row = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).get_attribute('innerText')
        basket_total = re.search(r'£(.+)', basket_total_row).group(1)
        self.basket_total = float(basket_total)
        print(basket_total)

    def should_add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_title_and_price_after_adding_to_basket(self):
        self.should_be_product_title_on_page_after_add_to_basket()
        self.should_be_equal_product_price_and_basket_cost()

    def should_be_product_title_on_page_after_add_to_basket(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE_ADDED)
        added_product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_ADDED).text
        product_name = self.product_title()
        assert product_name == added_product_title, "Заголовок товара и добавленного в корзину товара не совпадают"

    def should_be_equal_product_price_and_basket_cost(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.BASKET_COST)
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text.strip().replace('£', '')
        product_price = self.product_price()
        assert product_price + self.basket_total - float(
            basket_cost) < 10e-6, f"Цена товара и стоимость корзины не совпадают:" \
                                  f" стоимость корзины {basket_cost}," \
                                  f"цена товара {product_price}," \
                                  f"корзина до добавления {self.basket_total}"

    def should_be_no_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'element(message) is presented on page'

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "is not disappeared"

