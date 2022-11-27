from selenium.common import ElementClickInterceptedException, NoSuchElementException

from .login_page import LoginPage
from .products_page import ProductsPage
from .locators import ProductsPageLocators, BasketIconMainPageLocators, BasketPageLocators


class BasketPage(LoginPage, ProductsPage):

    def put_or_del_products_in_packet(self, item_names):
        """Метод добавления товаров в корзину с главной страницы сайта"""
        all_card_products = self.browser.find_elements(*ProductsPageLocators.INVENT_ITEM)
        product_name_add_basket = []
        for product in all_card_products:
            product_name = product.find_element(*ProductsPageLocators.NAME_PRODUCT).text
            if product_name in item_names:
                try:
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
        self.should_be_page_title('YOUR CART', *BasketPageLocators.TITLE)
        assert self.element_is_present(*BasketPageLocators.BASKET_LIST)
        product_in_basket = self.get_num_products_in_basket(*BasketPageLocators.LIST_PRODUCTS)
        assert num_product == len(product_in_basket), "Incorrect number of items in the cart"
