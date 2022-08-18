from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTAINS_ITEMS), "Basket is not empty"

    def basket_empty_message_should_exist(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "The message about empty basket doesn't exist"

        message_text = self.get_element_text(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        print("Message text: " + message_text)
        assert "Your basket is empty" in message_text, "The text about empty basket is not correct"
