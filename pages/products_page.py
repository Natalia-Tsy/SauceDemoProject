from .base_page import BasePage
from .locators import ProductsPageLocators
import re


class ProductsPage(BasePage):

    # Проверяет, что текущая страница является страницей корзины
    def should_be_products_page(self):

        # Проверяет, что текущая страница соответствует требованиям
        self.should_be_link("inventory")
        # Проверяет, что текст элемента заглавия страницы
        # соответствует требованиям
        self.should_be_page_title("PRODUCTS", *ProductsPageLocators.TITLE)
        # Проверяет, что товары на страницы соответствуют требованиям
        self.should_be_products_page_inventory_list()
        # Получает элемент корзины на странице
        assert self.browser.find_element(*ProductsPageLocators.SHOP_CART_LINK)

    # Проверяет, что товары на страницы соответствуют требованиям
    def should_be_products_page_inventory_list(self):
        # Получает список элементов товаров на странице
        list_el = self.browser.find_element(*ProductsPageLocators.INVENT_LIST)
        assert (
            len(list_el.get_property("children")) != 0
        ), "there is no products"

    def list_finded_item_by_name(self, item_names):
        # Получает список элементов товаров на странице
        list_el = self.browser.find_elements(*ProductsPageLocators.INVENT_ITEM)
        items = list(
            map(
                lambda y: list(
                    filter(lambda x: re.split("\\n", x.text)[0] == y, list_el)
                ),
                item_names,
            )
        )
        return items

    def click_button(self, el):
        # a = {}
        # print(type(el))
        inventory_item = el.get_property("children")
        # item_lbl = inventory_item[0].get_property("children")
        # pricebar = inventory_item[1].get_property("children")
        # h = pricebar[0].text
        # a[item_lbl[0].text] = pricebar[0].text
        inventory_item[1].get_property("children")[1].click()

    # Добавляется в корзину товар
    def add_item_on_products_page(self, *args, **kwargs):

        j = self.list_finded_item_by_name(args)
        list(filter(lambda x: list(map(lambda y: self.click_button(y), x)), j))
