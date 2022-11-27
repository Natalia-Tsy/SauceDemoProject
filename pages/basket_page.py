import time
import re
from selenium.common import ElementClickInterceptedException, NoSuchElementException

from .login_page import LoginPage
from .products_page import ProductsPage
from .locators import ProductsPageLocators, BasketIconMainPageLocators, CartPageLocators


class BasketPage(LoginPage, ProductsPage):

    def put_or_del_products_in_packet(self, item_names):
        """Метод добавления товаров в корзину с главной страницы сайта"""
        all_card_products = self.browser.find_elements(*ProductsPageLocators.INVENT_ITEM)
        product_name_add_basket = []
        for product in all_card_products:
            product_name = product.find_element(*ProductsPageLocators.NAME_PRODUCT).text
            if product_name in item_names:
                try:
                    time.sleep(4)
                    self.element_is_located_in_element(product, ProductsPageLocators.BTN_ADD_OR_DEL_TO_BASKET).click()
                    product_name_add_basket.append(product_name)
                except ElementClickInterceptedException:
                    return ElementClickInterceptedException
        return product_name_add_basket

    def view_and_remember_the_number_product_on_icon_basket(self):
        """Метод получения числа товаров в корзине после добавления товаров в корзину"""
        try:
            num_product_in_basket = self.browser.find_element(*BasketIconMainPageLocators.NUMBER_PRODUCT_IN_BASKET).text
        except NoSuchElementException:
            return 0
        return int(num_product_in_basket)

    def get_data_about_products_in_basket(self, num_product):
        """Метод получения данных со страницы корзины и сравнения товаров в корзине и на иконке корзины на главной странице"""
        self.click_button(*BasketIconMainPageLocators.ICON_BASKET)
        self.should_be_link('cart')
        self.should_be_page_title('YOUR CART', *CartPageLocators.TITLE)
        assert self.element_is_present(*CartPageLocators.BASKET_LIST)
        product_in_basket = self.get_num_products_in_basket(*CartPageLocators.LIST_PRODUCTS)
        assert num_product == len(product_in_basket), "Incorrect number of items in the cart"

    def get_ids_and_put_or_del_products_in_packet_on_the_card_page(self, item_names):
        """Метод добавления/удаления товаров с/из карточки товара в/из корзину(ы)"""
        all_card_products = self.browser.find_elements(*ProductsPageLocators.INVENT_ITEM)
        ids = [self.get_id_product(product) for product in all_card_products]
        for id in ids:
            self.add_or_del_product_from_card_product_page(id, item_names)

    def product_params_comparison_in_basket(self):
        """Метод проверки совпадения параметров товара в корзине"""
        name_product = "Sauce Labs Fleece Jacket"
        price_product = "49.99"
        products_in_basket = self.browser.find_elements(*CartPageLocators.PRODUCT_DIV)
        for product in products_in_basket:
            name_product_basket = product.find_element(*CartPageLocators.NAME_PRODUCT).text
            price_product_basket = self.clearing_characters("$", product.find_element(*CartPageLocators.PRICE_PRODUCT).text)
            assert name_product == name_product_basket, "The names of the products do not match"
            assert price_product == price_product_basket, "The price of the products do not match"
    def clear_all_products_in_basket(self):
        all_products_in_basket = self.browser.find_elements(*CartPageLocators.LIST_PRODUCTS)
        for product in all_products_in_basket:
            product.find_element(*CartPageLocators.DEL_PRODUCT_BTN).click()