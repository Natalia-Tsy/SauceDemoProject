from .base_page import BasePage
from .locators import Chckout2PageLocators


class CheckoutPage_2(BasePage):
    # Проверяет, что текущая страница является страницей корзины
    def should_be_checkout_2_page(self):
        # Проверяет, что текущая страница соответствует требованиям
        self.should_be_link("checkout-step-two")
        # Проверяет, что текст элемента заглавия страницы
        # соответствует требованиям
        self.should_be_page_title("CHECKOUT: OVERVIEW", *Chckout2PageLocators.TITLE)
        self.should_be_btn_to_checkout_complete_page()

    # Проверяет, что кнопка "FINISH" имеется на текущей странице
    def should_be_btn_to_checkout_complete_page(self):
        assert self.element_is_visible(Chckout2PageLocators.FINISH_BTN)

    # Переходит на страницу завершения оформления заказа
    def go_to_checkout_complete_page(self):
        self.click_button(*Chckout2PageLocators.FINISH_BTN)
