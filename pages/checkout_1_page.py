from .base_page import BasePage
from .locators import Chckout1PageLocators
from .src import Chckout1PageSrc


class CheckoutPage_1(BasePage):
    # Проверяет, что текущая страница является страницей корзины
    def should_be_checkout_1_page(self):
        # Проверяет, что текущая страница соответствует требованиям
        self.should_be_link(Chckout1PageSrc.LINK)
        # Проверяет, что текст элемента заглавия страницы
        # соответствует требованиям
        self.should_be_page_title(
            Chckout1PageSrc.TITLE, *Chckout1PageLocators.TITLE
        )
        self.should_be_input_firstname_to_checkout_1_page()
        self.should_be_input_lastname_to_checkout_1_page()
        self.should_be_input_postal_code_to_checkout_1_page()
        self.should_be_btn_to_checkout_1_page()

        # Проверяет, что элемент для ввода имени пользователя
        # имеется на текущей странице

    def should_be_input_firstname_to_checkout_1_page(self):
        assert self.element_is_present(*Chckout1PageLocators.INPUT_FIRSTNAME)

        # Проверяет, что элемент для ввода фамилии пользователя
        # имеется на текущей странице

    def should_be_input_lastname_to_checkout_1_page(self):
        assert self.element_is_present(*Chckout1PageLocators.INPUT_LASTNAME)

        # Проверяет, что элемент для ввода кода получения
        # имеется на текущей странице

    def should_be_input_postal_code_to_checkout_1_page(self):
        assert self.element_is_present(*Chckout1PageLocators.INPUT_CODE)

    # Проверяет, что кнопка "CHECKOUT" имеется на текущей странице
    def should_be_btn_to_checkout_1_page(self):
        assert self.element_is_visible(Chckout1PageLocators.CONTINUE_BTN)

    # Заполняются данные, необходимые для получения товара
    def set_shipping_info(self, firstname, lastname, code):
        # Имя пользователя передается текстовому элементу на странице
        self.browser.find_element(*Chckout1PageLocators.INPUT_FIRSTNAME).send_keys(
            firstname
        )
        # Пароль передается текстовому элементу на странице
        self.browser.find_element(*Chckout1PageLocators.INPUT_LASTNAME).send_keys(
            lastname
        )
        # Код получения передается текстовому элементу на странице
        self.browser.find_element(*Chckout1PageLocators.INPUT_CODE).send_keys(code)

    # Нажимается кнопка "LOGIN"
    def go_to_checkout_2_page(self):
        self.click_button(*Chckout1PageLocators.CONTINUE_BTN)
