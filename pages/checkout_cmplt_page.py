from .base_page import BasePage
from .locators import CheckoutCmpltPageLocators
from .src import CheckoutCmpltPageSrc
from .locators import PageLocators


class CheckouCmpltPage(BasePage):
    # Checks that the current page is Checkout-complete Page
    def should_be_checkout_complete_page(self):
        # Checks that the current page meets the requirements
        self.should_be_link(CheckoutCmpltPageSrc.LINK)
        # Checks that the text of the page title element meets the requirements
        self.should_be_page_title(
            CheckoutCmpltPageSrc.TITLE, *CheckoutCmpltPageLocators.TITLE
        )
        self.should_be_btn_to_checkout_complete_page()
        self.should_be_empty_shopping_cart_badge()

    # Checks there's 'Back-home' button on the page
    def should_be_btn_to_checkout_complete_page(self):
        assert self.element_is_visible(CheckoutCmpltPageLocators.BACKHOME_BTN)

    # Checks that the cart icon doesn't display any products
    def should_be_empty_shopping_cart_badge(self):
        el = self.browser.find_element(*CheckoutCmpltPageLocators.SHOP_CART_LINK)
        assert (el.get_property("children")) == [], "there is some items in cart"

    # Goes to the page to complete the order
    def go_to_products_page(self):
        self.click_button(*CheckoutCmpltPageLocators.BACKHOME_BTN)

    # Checks the link Privacy Policy
    def check_privacy_link(self):
        assert self.element_is_present(*PageLocators.ROBOT_IMG), "something went wrong"
        self.browser.find_element(*PageLocators.PRIVACY).click()
