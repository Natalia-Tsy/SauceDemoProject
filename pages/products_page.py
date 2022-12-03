import re
from .base_page import BasePage
from .locators import ProductsPageLocators
from .src import ProductsPageSrc
from .locators import PageLocators


class ProductsPage(BasePage):

    # Checks that the current page is Products page
    def should_be_products_page(self):
        # Checks that the current page meets the requirements
        self.should_be_link(ProductsPageSrc.LINK)
        # Checks that the page title element meets the requirements
        self.should_be_page_title(ProductsPageSrc.TITLE, *ProductsPageLocators.TITLE)
        # Checks that the products on the page meet the requirements
        self.should_be_products_page_inventory_list()
        # Checks that there's a link to the Cart
        self.should_be_link_to_cart_page()

    # Checks that there's a link to the Cart
    def should_be_link_to_cart_page(self):
        # assert self.element_is_located(*ProductsPageLocators.SHOP_CART_LINK)
        assert self.element_is_visible(ProductsPageLocators.SHOP_CART_LINK)

    # Checks the products on the page meet the requirements
    def should_be_products_page_inventory_list(self):
        # Gets the list of elements on the page
        list_el = self.browser.find_element(*ProductsPageLocators.INVENT_LIST)
        assert len(list_el.get_property("children")) != 0, "there is no products"

    # Products on the page are searched in accordance with the requirements
    def list_finded_item_by_name(self, item_names):
        # Gets the list of products on the page
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

    # The button  "ADD TO CART"/"REMOVE" is pressed for the selected products
    def find_button(self, el):
        # Product module
        inventory_item = el.get_property("children")
        # Product Pricebar module
        pricebar = inventory_item[1].get_property("children")
        #  "ADD TO CART"/"REMOVE" button
        btn_inventory = pricebar[1]
        btn_inventory.click()

    # Products are added into the cart in accordance with the requirements
    def add_item_on_products_page(self, *args, **kwargs):
        selected_items = self.flatten(self.list_finded_item_by_name(args))
        # Products are added into the cart one by one
        list(map(lambda y: self.find_button(y), selected_items))
        return selected_items

    # Goes to the Cart page
    def go_to_basket_page(self):
        self.click_button(*ProductsPageLocators.SHOP_CART_LINK)

    # Check the cart icon on the current page doesn't display any products
    def should_be_empty_shopping_cart_badge(self):
        el = self.browser.find_element(*ProductsPageLocators.SHOP_CART_LINK)
        assert (el.get_property("children")) == [], "there is some items in cart"

    # Checks the link Privacy Policy
    def check_privacy_link(self):
        assert self.element_is_present(*PageLocators.ROBOT_IMG), "something went wrong"
        # self.browser.find_element(*PageLocators.PRIVACY)
        self.click_button(*PageLocators.PRIVACY)

    """Check choose product:
        Product image
        Product name = "Sauce Labs Bike Light"
        Price = $9.99"""

    def select_product(self):
        item_info = {}
        item_info["img"] = self.get_src(0, *ProductsPageLocators.PRODUCT_IMG)
        item_info["name"] = self.get_text(0, *ProductsPageLocators.PRODUCT_NAME)
        item_info["price"] = self.get_text(0, *ProductsPageLocators.PRODUCT_PRICE)
        return item_info

    def go_to_product_page(self):
        self.click_button(*ProductsPageLocators.PRODUCT_IMG)

    # sort products by name
    def sorting_products_by_name_asc(self):
        new_list_before_sorting = self.get_text_elements(
            0, *ProductsPageLocators.ALL_NAMES
        )
        if new_list_before_sorting == []:
            assert False, "We have a problem!"
        new_list_before_sorting.sort()
        sorting_products_by_name_asc = self.browser.find_element(
            *ProductsPageLocators.SORTING_BY_NAME_AZ
        )
        sorting_products_by_name_asc.click()
        new_list_all_name_after_sorting = self.get_text_elements(
            0, *ProductsPageLocators.ALL_NAMES
        )
        assert (
            new_list_before_sorting == new_list_all_name_after_sorting
        ), "We have a problem!"

    def sorting_products_by_price_asc(self):
        new_list_for_sort_without_first_symbol = self.get_text_elements(
            1, *ProductsPageLocators.All_PRICES
        )
        if new_list_for_sort_without_first_symbol == []:
            assert False, " Error"
        new_list_for_sort_without_first_symbol = list(
            map(float, new_list_for_sort_without_first_symbol)
        )
        new_list_for_sort_without_first_symbol.sort()
        sorting_products_by_name_asc = self.browser.find_element(
            *ProductsPageLocators.SORTING_BY_PRICE_ASC
        )
        sorting_products_by_name_asc.click()
        new_list_all_price_after_sorting = self.get_text_elements(
            1, *ProductsPageLocators.All_PRICES
        )
        new_list_all_price_after_sorting = list(
            map(float, new_list_all_price_after_sorting)
        )

        assert (
            new_list_for_sort_without_first_symbol == new_list_all_price_after_sorting
        ), " Error"
