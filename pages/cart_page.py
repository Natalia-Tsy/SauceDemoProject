from .base_page import BasePage
from .locators import CartPageLocators
from .src import CartPageSrc


class CartPage(BasePage):

    # Проверяет, что текущая страница является страницей корзины
    def should_be_cart_page(self):
        # Проверяет, что текущая страница соответствует требованиям
        self.should_be_link(CartPageSrc.LINK)
        # Проверяет, что текст элемента заглавия страницы
        # соответствует требованиям
        self.should_be_page_title(CartPageSrc.TITLE, *CartPageLocators.TITLE)
        # Проверяет, что кнопка "CHECKOUT" имеется на странице
        self.should_be_btn_to_checkout_1_page()

    # Проверяет, что кнопка "CHECKOUT" имеется на странице
    def should_be_btn_to_checkout_1_page(self):
        assert self.element_is_visible(CartPageLocators.CHECKOUT_BTN)

    # Переходит на страницу корзины
    def go_to_checkout_1_page(self):
        self.click_button(*CartPageLocators.CHECKOUT_BTN)
