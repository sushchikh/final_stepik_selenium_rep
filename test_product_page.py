from .pages.product_page import AddToBasket
from .pages.base_page import BasePage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = AddToBasket(browser, link)
    page.open()
    page.add_to_cart_btn()
    page.solve_quiz_and_get_code()
    page.check_name_and_price()
