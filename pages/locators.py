from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_LINK = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_IN_CART = (By.CSS_SELECTOR, "div.alertinner > strong")
    NAME_IN_ITEM_PLACEHOLDER = (By.CSS_SELECTOR, "div#content_inner h1")
    PRICE_IN_CART = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    PRICE_IN_ITEM_PLACEHOLDER = (By.CSS_SELECTOR, "p.price_color")
