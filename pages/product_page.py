import math
from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators
from time import sleep


class AddToBasket(BasePage):

    def add_to_cart_btn(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_LINK)
        link.click()
        # sleep(5)
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        print(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        sleep(10)

    def check_name_and_price(self):
        name_in_cart = self.browser.find_element(*ProductPageLocators.NAME_IN_CART).text
        print('название товара в корзине: ', name_in_cart)
        name_in_item_placeholder = self.browser.find_element(*ProductPageLocators.NAME_IN_ITEM_PLACEHOLDER).text
        print('название товара в описании: ', name_in_item_placeholder)
        assert name_in_item_placeholder == name_in_cart, "name in cart != name in item placeholder"

        price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        print('цена в корзине:', price_in_cart)
        price_in_item_placeholder = self.browser.find_element(*ProductPageLocators.PRICE_IN_ITEM_PLACEHOLDER).text
        print('цена товара в описании: ', price_in_item_placeholder)
        assert  price_in_item_placeholder == price_in_cart, "price in cart != price in item placeholder"