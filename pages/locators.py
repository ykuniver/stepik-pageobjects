from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")

    PRODUCT_NAME_IN_PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_IN_PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".product_main > .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    PRODUCT_NAME_IN_RESULT_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE_IN_RESULT_MESSAGE = (By.CSS_SELECTOR, ".alertinner > p > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    BASKET_CONTAINS_ITEMS = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p')
