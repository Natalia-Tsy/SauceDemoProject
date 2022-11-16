import re
from .base_page import BasePage
from .locators import ProductsPageLocators
from .src import ProductsPageSrc


class ProductsPage(BasePage):

    # Проверяет, что текущая страница является страницей корзины
    def should_be_products_page(self):

        # Проверяет, что текущая страница соответствует требованиям
        self.should_be_link(ProductsPageSrc.LINK)
        # Проверяет, что текст элемента заглавия страницы
        # соответствует требованиям
        self.should_be_page_title(ProductsPageSrc.TITLE, *ProductsPageLocators.TITLE)
        # Проверяет, что товары на страницы соответствуют требованиям
        self.should_be_products_page_inventory_list()
        # Проверяет, что имеется ссылка на страницу корзины
        self.should_be_link_to_cart_page()

    # Проверяет, что имеется ссылка на страницу корзины
    def should_be_link_to_cart_page(self):
        # assert self.element_is_located(*ProductsPageLocators.SHOP_CART_LINK)
        assert self.element_is_visible(ProductsPageLocators.SHOP_CART_LINK)

    # Проверяет, что товары на страницы соответствуют требованиям
    def should_be_products_page_inventory_list(self):
        # Получает список элементов товаров на странице
        list_el = self.browser.find_element(*ProductsPageLocators.INVENT_LIST)
        assert len(list_el.get_property("children")) != 0, "there is no products"

    # Выполняется поиск элементов товаров на странице в соответствии с требованиями
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

    # Нажимается кнопка "ADD TO CART"/"REMOVE" выбранных элементов товаров
    def find_button(self, el):
        # Блок товара
        inventory_item = el.get_property("children")
        # Блок pricebar товара
        pricebar = inventory_item[1].get_property("children")
        # Кнопка "ADD TO CART"/"REMOVE" товара
        btn_inventory = pricebar[1]
        btn_inventory.click()

    # Добавляются товары в корзину в соответствии с требованием
    def add_item_on_products_page(self, *args, **kwargs):
        selected_items = self.flatten(self.list_finded_item_by_name(args))
        # Добавляется поочередно товар в корзину товар
        list(map(lambda y: self.find_button(y), selected_items))
        return selected_items

    # Переходит на страницу корзины
    def go_to_basket_page(self):
        self.click_button(*ProductsPageLocators.SHOP_CART_LINK)

    # Проверяет, что иконка корзины на текущей странице не указывает количество
    # товаров в корзине
    def should_be_empty_shopping_cart_badge(self):
        el = self.browser.find_element(*ProductsPageLocators.SHOP_CART_LINK)
        assert (el.get_property("children")) == [], "there is some items in cart"
