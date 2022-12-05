from .base_page import BasePage
from .locators import CartPageLocators
from .src import CartPageSrc
from .locators import PageLocators


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
        self.browser.find_element(*PageLocators.HAMBURGER).click()

    # Top left menu "all items" line
    def click_all_items(self):
        self.element_is_visible(PageLocators.ALL_ITEMS)
        self.browser.find_element(*PageLocators.ALL_ITEMS).click()

    # Select and click LOGOUT item from hamburger menu
    def click_logout_from_top_left_menu(self):
        self.open_hamburger()
        self.element_is_visible(PageLocators.LOGOUT)
        self.browser.find_element(*PageLocators.LOGOUT).click()

    # Clear cart
    def clear_cart(self):
        # Gets the list of elements on the cart page
        list_el = self.browser.find_elements(*CartPageLocators.LIST_OF_REMOVE_BUTTON_ELEMENTS)
        while len(list_el) > 0:
            list_el[0].click()
            list_el = self.browser.find_elements(*CartPageLocators.LIST_OF_REMOVE_BUTTON_ELEMENTS)

    # Check that this item is presents in the cart
    def check_this_item_is_presents_in_the_cart(self, item):
        assert_cond = False
        list_name_el = \
            self.browser.find_elements(*CartPageLocators.LIST_OF_NAME_PRODUCTS)
        for element in list_name_el:
            if element.text == item:
                assert_cond = True
                break
        assert assert_cond, "Selected Item is no presents in the cart"
