from .base_page import BasePage
from .locators import CheckoutCmpltPageLocators


class CheckouCmpltPage(BasePage):
    # Проверяет, что текущая страница является страницей корзины
    def should_be_checkout_complete_page(self):
        # Проверяет, что текущая страница соответствует требованиям
        self.should_be_link("checkout-complete")
        # Проверяет, что текст элемента заглавия страницы
        # соответствует требованиям
        self.should_be_page_title(
            "CHECKOUT: COMPLETE!", *CheckoutCmpltPageLocators.TITLE
        )
        self.should_be_btn_to_checkout_complete_page()
        self.should_be_empty_shopping_cart_badge()

    # Проверяет, что кнопка "FINISH" имеется на текущей странице
    def should_be_btn_to_checkout_complete_page(self):
        assert self.element_is_visible(CheckoutCmpltPageLocators.BACKHOME_BTN)

    # Проверяет, что иконка корзины не указывает количество товаров в корзине
    def should_be_empty_shopping_cart_badge(self):
        el = self.browser.find_element(
            *CheckoutCmpltPageLocators.SHOP_CART_LINK
        )
        assert (
            el.get_property("children")
        ) == [], "there is some items in cart"

    # Переходит на страницу завершения оформления заказа
    def go_to_products_page(self):
        self.click_button(*CheckoutCmpltPageLocators.BACKHOME_BTN)
