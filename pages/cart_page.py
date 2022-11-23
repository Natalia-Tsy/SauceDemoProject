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
