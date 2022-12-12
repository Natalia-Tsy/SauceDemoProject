from .base_page import BasePage
from .locators import PageLocators, CartPageLocators, SideBarLocator
from src.src import CartPageSrc


class CartPage(BasePage):
    """This class is used to test the functionality of the cart page of the website

    Args:
        BasePage: Contains common methods that are used by all page classes
    """

    def should_be_cart_page(self):
        """Check that the current page is the cart page."""
        self.should_be_link(CartPageSrc.LINK)
        self.should_be_page_title(CartPageSrc.TITLE, *CartPageLocators.TITLE)
        self.should_be_btn_to_checkout_1_page()

    def should_be_btn_to_checkout_1_page(self):
        """Check that the checkout button is present and visible on the current page."""
        assert self.element_is_visible(
            CartPageLocators.CHECKOUT_BTN
        ), "The checkout button is not present or not visible on the page"

    def go_to_checkout_1_page(self):
        """Navigate to the first checkout page."""
        self.click_button(*CartPageLocators.CHECKOUT_BTN)

    def check_privacy_link(self):
        """Check that the privacy link is present on the page
        and that it can be clicked to navigate to the privacy policy page.
        """
        assert self.element_is_present(
            *PageLocators.ROBOT_IMG
        ), "The footer_robot is not present on the page"
        self.browser.find_element(*PageLocators.PRIVACY).click()

    def check_the_quantity(self):
        """Check the quantity of items in the cart"""
        quant = self.browser.find_element(*CartPageLocators.QUANTITY).text
        if quant != 0:
            assert "There are items in the cart", "the cart is empty"

    def open_hamburger(self):
        """Open the hamburger menu on the current page."""
        self.browser.find_element(*SideBarLocator.HAMBURGER).click()

    def click_all_items(self):
        """Check that the "All items" link is present and visible on the current page
        and that it can be the clicked in the hamburger menu on the current page."""
        self.element_is_visible(SideBarLocator.ALL_ITEMS)
        self.browser.find_element(*SideBarLocator.ALL_ITEMS).click()

    def clear_cart(self):
        """Find all of the "REMOVE" buttons on the cart page and then clicks on them one by one in the cart."""
        # Gets the list of elements on the cart page
        list_el = self.browser.find_elements(
            *CartPageLocators.LIST_OF_REMOVE_BUTTON_ELEMENTS
        )
        while len(list_el) > 0:
            list_el[0].click()
            list_el = self.browser.find_elements(
                *CartPageLocators.LIST_OF_REMOVE_BUTTON_ELEMENTS
            )

    def check_product_name_in_cart(self, item_name):
        """Check the name of a specific product in the cart.

        Args:
            item_name: expected product
        """
        list_el = self.browser.find_elements(*CartPageLocators.LIST_OF_PRODUCTS)
        for element in list_el:
            name = element.find_element(*CartPageLocators.PRODUCT_NAME_OF_ITEM).text
            assert (
                name == item_name
            ), f"Expected product {item_name} is not present in the cart"
            break

    def check_the_item_quantity_in_cart(self, item_name, item_qty):
        """Check the quantity of a specific product in the cart.

        Args:
            item_name: expected product
            item_qty:  expected quantity
        """
        list_el = self.browser.find_elements(*CartPageLocators.LIST_OF_PRODUCTS)
        for element in list_el:
            name = element.find_element(*CartPageLocators.PRODUCT_NAME_OF_ITEM).text
            qty = element.find_element(*CartPageLocators.QTY_OF_ITEM).text
            if name == item_name:
                assert (
                    qty == item_qty
                ), f"Expected product is found, but quantity {qty} doesn't match the expected quantity {item_qty}"
                break

    # Check that item with item_name is presents in the cart with price item_price
    def check_the_item_price_in_cart(self, item_name, item_price):
        """Check the price of a specific product in the cart.

        Args:
            item_name: expected product
            item_price: expected price
        """
        list_el = self.browser.find_elements(*CartPageLocators.LIST_OF_PRODUCTS)
        for element in list_el:
            name = element.find_element(*CartPageLocators.PRODUCT_NAME_OF_ITEM).text
            price = element.find_element(*CartPageLocators.PRICE_OF_ITEM).text
            if name == item_name:
                assert (
                    price == item_price
                ), f"Expected product is found, but price {price} doesn't match the expected price {item_price}"
                break
