import re
from .base_page import BasePage
from src.src import ProductsPageSrc
from .locators import PageLocators, ProductsPageLocators


class ProductsPage(BasePage):
    """This class is used to test the functionality of the products page of the website.

    Args:
        BasePage: Contains common methods that are used by all page classes
    """

    def should_be_products_page(self):
        """Check that the current page is the products page."""
        self.should_be_link(ProductsPageSrc.LINK)
        self.should_be_page_title(ProductsPageSrc.TITLE, *ProductsPageLocators.TITLE)
        self.should_be_products_page_inventory_list()
        self.should_be_link_to_cart_page()

    def should_be_link_to_cart_page(self):
        """Check the shopping cart link is visible on the page."""
        assert self.element_is_visible(
            ProductsPageLocators.SHOP_CART_LINK
        ), "The shopping cart link is not present or not visible on the page"

    def should_be_products_page_inventory_list(self):
        """Checks products in an inventory list on the page."""
        value = self.get_property("children", *ProductsPageLocators.INVENT_LIST)
        assert value is not None, "The inventory list could not be found on the page"
        assert len(value) != 0, "No products in the inventory list"

    def list_finded_item_by_name(self, item_names):
        """Returns a list of products on the products page that match the item_names.

        Args:
            item_names: names of the products

        Returns:
            list[selenium.webdriver.remote.webelement.WebElement]: the list of items
        """
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

    def find_button(self, el):
        """Find and click the button "ADD TO CART"/"REMOVE" of selected element on the products page.

        Args:
            selenium.webdriver.remote.webelement.WebElement: selected item
        """
        # Product module
        inventory_item = el.get_property("children")
        # Product Pricebar module
        pricebar = inventory_item[1].get_property("children")
        #  "ADD TO CART"/"REMOVE" button
        btn_inventory = pricebar[1]
        btn_inventory.click()

    # Products are added into the cart in accordance with the requirements
    def add_item_on_products_page(self, *args, **kwargs):
        """Add items to the cart or remove items from cart by name.

        Returns:
            list[selenium.webdriver.remote.webelement.WebElement]: list of the selected items by name
        """
        selected_items = self.flatten(self.list_finded_item_by_name(args))
        # Products are added into the cart one by one
        list(map(lambda y: self.find_button(y), selected_items))
        return selected_items

    def go_to_basket_page(self):
        """Navigate to the cart page."""
        self.click_button(*ProductsPageLocators.SHOP_CART_LINK)

    def should_be_empty_shopping_cart_badge(self):
        """Check the cart is empty."""
        value = self.get_property("children", *ProductsPageLocators.SHOP_CART_LINK)
        assert value is not None, "The shopping cart is not present on the page"
        assert value == [], "The shopping cart is not empty"

    def check_privacy_link(self):
        """Check that the privacy link is present on the page
        and that it can be clicked to navigate to the privacy policy page."""
        assert self.element_is_present(
            *PageLocators.ROBOT_IMG
        ), "The footer_robot is not present on the page"
        self.browser.find_element(*PageLocators.PRIVACY).click()

    """Check choose product:
        Product image
        Product name = "Sauce Labs Bike Light"
        Price = $9.99"""

    def select_product(self):
        """Retrieve the information about a product on the products page.

        Returns:
            dict: dictionary containing information about a product on the products page
        """
        item_info = {}
        item_info["img"] = self.get_src(0, *ProductsPageLocators.PRODUCT_IMG)
        item_info["name"] = self.get_text(0, *ProductsPageLocators.PRODUCT_NAME)
        item_info["price"] = self.get_text(0, *ProductsPageLocators.PRODUCT_PRICE)
        return item_info

    def go_to_product_page(self):
        """Navigate to the selected product page."""
        self.click_button(*ProductsPageLocators.PRODUCT_IMG)

    def sorting_products_by_name_asc(self):
        """Sort a list of products by name in ascending order and check the sorting."""
        new_list_before_sorting = self.get_text_elements(
            0, *ProductsPageLocators.INVENTORY_ITEM_NAME
        )
        if new_list_before_sorting == []:
            assert False, "Items could not are found on the products page"
        new_list_before_sorting.sort()
        sorting_products_by_name_asc = self.browser.find_element(
            *ProductsPageLocators.SORTING_BY_NAME_AZ
        )
        sorting_products_by_name_asc.click()
        new_list_all_name_after_sorting = self.get_text_elements(
            0, *ProductsPageLocators.INVENTORY_ITEM_NAME
        )
        assert (
            new_list_before_sorting == new_list_all_name_after_sorting
        ), "The list of product names on the page isn't the same as the sorted list by name in ascending order"

    def sorting_products_by_price_asc(self):
        """Sorts a list of products by price in ascending order and check the sorting."""
        new_list_for_sort_without_first_symbol = self.get_text_elements(
            1, *ProductsPageLocators.INVENTORY_ITEM_PRICE
        )
        if new_list_for_sort_without_first_symbol == []:
            assert False, "Items could not are found on the products page"
        new_list_for_sort_without_first_symbol = list(
            map(float, new_list_for_sort_without_first_symbol)
        )
        new_list_for_sort_without_first_symbol.sort()
        sorting_products_by_name_asc = self.browser.find_element(
            *ProductsPageLocators.PRICE_LOW_TO_HIGH
        )
        sorting_products_by_name_asc.click()
        new_list_all_price_after_sorting = self.get_text_elements(
            1, *ProductsPageLocators.INVENTORY_ITEM_PRICE
        )
        new_list_all_price_after_sorting = list(
            map(float, new_list_all_price_after_sorting)
        )
        assert (
            new_list_for_sort_without_first_symbol == new_list_all_price_after_sorting
        ), "The list of product prices on the page isn't the same as the sorted list by price in ascending order"
