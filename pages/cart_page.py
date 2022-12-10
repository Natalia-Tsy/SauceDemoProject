from .base_page import BasePage
from .locators import CartPageLocators
from .src import CartPageSrc
from .locators import PageLocators
from .locators import SideBarLocator


class CartPage(BasePage):

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
