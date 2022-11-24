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
    def check_footer(self):
        assert self.element_is_present(*PageLocators.ROBOT), "something went wrong"
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
