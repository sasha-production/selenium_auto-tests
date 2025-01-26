from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "there are items in basket"

    def should_be_message_that_basket_is_empty(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert 'basket is empty' in message, "message is not correct, basket should be empty"
