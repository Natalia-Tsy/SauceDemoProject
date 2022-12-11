import logging

from selenium.common import NoSuchElementException, ElementClickInterceptedException

from .locators import CartPageLocators, CardProductPageLocator, ProductsPageLocators
from .locators import PageLocators
from .locators import SideBarLocator
from .login_page import LoginPage
from .products_page import ProductsPage
from .src import CartPageSrc


class CartPage(LoginPage, ProductsPage):

    # Checks that the page is Cart page
    def should_be_cart_page(self):
        # Checks that the current page meets the requirements
        self.should_be_link(CartPageSrc.LINK)
        # Checks that the text of the title element meets the requirements
        self.should_be_page_title(CartPageSrc.TITLE, *CartPageLocators.TITLE)
        # Checks there's "checkout" button on the page
        self.should_be_btn_to_checkout_1_page()

    # Checks there's "checkout" button on the page
    def should_be_btn_to_checkout_1_page(self):
        assert self.element_is_visible(CartPageLocators.CHECKOUT_BTN)

    # Goes to Checkout-1 page
    def go_to_checkout_1_page(self):
        self.click_button(*CartPageLocators.CHECKOUT_BTN)

    # Checks the link Privacy Policy
    def check_privacy_link(self):
        assert self.element_is_present(*PageLocators.ROBOT_IMG), "something went wrong"
        self.browser.find_element(*PageLocators.PRIVACY).click()

    def check_the_quantity(self):
        quant = self.browser.find_element(*CartPageLocators.QUANTITY).text
        if quant != 0:
            assert "there are items in the cart", "the cart is empty"

    # Opens hamburger menu
    def open_hamburger(self):
        self.browser.find_element(*SideBarLocator.HAMBURGER).click()

    # Top left menu "all items" line
    def click_all_items(self):
        self.element_is_visible(SideBarLocator.ALL_ITEMS)
        self.browser.find_element(*SideBarLocator.ALL_ITEMS).click()

    # Clear cart
    def clear_cart(self):
        # Gets the list of elements on the cart page
        list_el = self.browser.find_elements(
            *CartPageLocators.LIST_OF_REMOVE_BUTTON_ELEMENTS
        )
        while len(list_el) > 0:
            list_el[0].click()
            list_el = self.browser.find_elements(
                *CartPageLocators.LIST_OF_REMOVE_BUTTON_ELEMENTS
            )

    # Check that item with item_name is presents in the cart
    def check_product_name_in_cart(self, item_name):
        list_el = self.browser.find_elements(*CartPageLocators.LIST_OF_PRODUCTS)
        for element in list_el:
            name = element.find_element(*CartPageLocators.PRODUCT_NAME_OF_ITEM).text
            assert (
                name == item_name
            ), f"Ожидаемый товар {item_name} в корзине отсутствует"
            break

    # Check that item with item_name is presents in the cart with item_qty quantity
    def check_the_item_quantity_in_cart(self, item_name, item_qty):
        list_el = self.browser.find_elements(*CartPageLocators.LIST_OF_PRODUCTS)
        for element in list_el:
            name = element.find_element(*CartPageLocators.PRODUCT_NAME_OF_ITEM).text
            qty = element.find_element(*CartPageLocators.QTY_OF_ITEM).text
            if name == item_name:
                assert (
                    qty == item_qty
                ), f"Товар ожидаемый, но кол-во {qty} не соответствует ожидаемому {item_qty}"
                break

    # Check that item with item_name is presents in the cart with price item_price
    def check_the_item_price_in_cart(self, item_name, item_price):
        list_el = self.browser.find_elements(*CartPageLocators.LIST_OF_PRODUCTS)
        for element in list_el:
            name = element.find_element(*CartPageLocators.PRODUCT_NAME_OF_ITEM).text
            price = element.find_element(*CartPageLocators.PRICE_OF_ITEM).text
            if name == item_name:
                assert (
                    price == item_price
                ), f"Товар ожидаемый, но цена {price} не соответствует ожидаемой {item_price}"
                break

    def put_or_del_products_in_packet(self, item_names):
        """The method of adding/del products to the cart from the main page of the site"""
        all_card_products = self.browser.find_elements(
            *ProductsPageLocators.INVENT_ITEM
        )
        product_name_add_basket = []
        for product in all_card_products:
            product_name = product.find_element(*ProductsPageLocators.NAME_PRODUCT).text
            if product_name in item_names:
                try:
                    self.element_is_located_in_element(
                        product, ProductsPageLocators.BTN_ADD_OR_DEL_TO_BASKET
                    ).click()
                    product_name_add_basket.append(product_name)
                except ElementClickInterceptedException as e:
                    logging.error(
                        f"Could not clicked elements on page: '{self.browser.current_url}'"
                    )
                    logging.exception(e.msg)
                    return ElementClickInterceptedException
        return product_name_add_basket

    def view_and_remember_the_number_product_on_icon_basket(self):
        """Method of getting the number of products in the basket after adding products to the basket"""
        try:
            num_product_in_basket = self.browser.find_element(
                *ProductsPageLocators.NUMBER_PRODUCT_IN_BASKET
            ).text
        except NoSuchElementException as e:
            logging.error(
                f"Could not find elements on page: '{self.browser.current_url}'"
            )
            logging.exception(e.msg)
            return 0
        return int(num_product_in_basket)

    def get_data_about_products_in_basket(self, num_product):
        """Method of getting data from the cart page and comparing products in the cart and on the cart icon on the main
        page"""
        self.go_to_basket_page()
        self.should_be_cart_page()
        assert self.element_is_present(*CartPageLocators.BASKET_LIST)
        product_in_basket = self.get_num_products_in_basket(
            *CartPageLocators.LIST_PRODUCTS
        )
        assert num_product == len(
            product_in_basket
        ), "Incorrect number of items in the cart"

    def get_id_product(self, element):
        """Method of obtaining the product ID"""
        product_id = (
            element.find_element(*ProductsPageLocators.PRODUCT_ID)
            .get_attribute("id")
            .split("_title_link")[0]
            .split("item_")[1]
        )
        return product_id

    def add_or_del_product_from_card_product_page(self, product_id):
        """Method of adding/removing products from/from the product card to/from the cart(s)"""
        url = f"https://www.saucedemo.com/inventory-item.html?id={product_id}"
        self.browser.get(url)
        try:
            self.browser.find_element(*CardProductPageLocator.ADD_BTN).click()
        except NoSuchElementException as e:
            self.browser.find_element(*CardProductPageLocator.DEL_BTN).click()
            logging.error(
                f"Could not find elements on page: '{self.browser.current_url}'"
            )
            logging.exception(e.msg)
        self.browser.find_element(
            *CardProductPageLocator.BACK_TO_THE_MAIN_PAGE_BTN
        ).click()

    def get_ids_and_put_or_del_products_in_packet_on_the_card_page(self, item_names):
        """Method of adding/removing products from/from the product card to/from the cart(s)"""
        all_card_products = self.list_finded_item_by_name(item_names)[0]
        ids = [self.get_id_product(product) for product in all_card_products]
        for id in ids:
            self.add_or_del_product_from_card_product_page(id)

    def product_params_comparison_in_basket(self):
        """The method of checking the coincidence of the parameters of the product in the basket"""
        all_data = [
            ("Sauce Labs Backpack", "29.99"),
            ("Sauce Labs Bolt T-Shirt", "15.99"),
            ("Sauce Labs Fleece Jacket", "49.99"),
            ("Test.allTheThings() T-Shirt (Red)", "15.99"),
        ]
        products_in_basket = self.browser.find_elements(*CartPageLocators.PRODUCT_DIV)
        for product in products_in_basket:
            name_product_basket = product.find_element(
                *CartPageLocators.NAME_PRODUCT
            ).text
            price_product_basket = self.clearing_characters(
                "$", product.find_element(*CartPageLocators.PRICE_PRODUCT).text
            )
            assert (
                name_product_basket,
                price_product_basket,
            ) in all_data, "The names or price of the products do not match"

    def check_number_products_in_basket_is_zero(self):
        """Method of checking that all products are removed from the basket"""
        product_in_basket = self.get_num_products_in_basket(
            *CartPageLocators.LIST_PRODUCTS
        )
        assert 0 == len(product_in_basket), "Incorrect number of items in the cart"
