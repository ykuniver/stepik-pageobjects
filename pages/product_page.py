import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add_to_basket.click()

    def product_name_in_result_match_product_name_in_description(self):
        product_name_in_desc = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_PRODUCT_DESCRIPTION).text
        print("Name in desc: " + product_name_in_desc)

        product_name_in_result = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_RESULT_MESSAGE).text
        print("Name in result: " + product_name_in_result)

        assert_message = "The product names in description and message result don't match!"
        assert product_name_in_desc == product_name_in_result, assert_message

    def price_in_result_match_price_in_description(self):
        price_in_desc = self.browser.find_element(*ProductPageLocators.PRICE_IN_PRODUCT_DESCRIPTION).text
        print("Price in desc: " + price_in_desc)

        price_in_result = self.browser.find_element(*ProductPageLocators.PRICE_IN_RESULT_MESSAGE).text
        print("Price in result: " + price_in_result)

        assert_message = "The prices in description and message result don't match!"
        assert price_in_desc == price_in_result, assert_message

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def element_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message got disappeared"
