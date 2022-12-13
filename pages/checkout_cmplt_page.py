from .base_page import BasePage
from .locators import PageLocators, CheckoutCmpltPageLocators
from src.src import CheckoutCmpltPageSrc


class CheckouCmpltPage(BasePage):
    """This class is used to test the functionality of the checkout complete page of the website.

    Args:
        BasePage: Contains common methods that are used by all page classes
    """

    def should_be_checkout_complete_page(self):
        """Check that the current page is the checkout complete page."""
        self.should_be_link(CheckoutCmpltPageSrc.LINK)
        self.should_be_page_title(
            CheckoutCmpltPageSrc.TITLE, *CheckoutCmpltPageLocators.TITLE
        )
        self.should_be_btn_to_checkout_complete_page()
        self.should_be_empty_shopping_cart_badge()

    def should_be_btn_to_checkout_complete_page(self):
        """Check the "BACKHOME" button is visible on the page."""
        assert self.element_is_visible(
            CheckoutCmpltPageLocators.BACKHOME_BTN
        ), "The backhome button is not present or not visible on the page"

    def should_be_empty_shopping_cart_badge(self):
        """Check the cart is empty."""
        value = self.get_property("children", *CheckoutCmpltPageLocators.SHOP_CART_LINK)
        assert value is not None, "The shopping cart is not present on the page"
        assert value == [], "The shopping cart is not empty"

    def go_to_products_page(self):
        """Navigate to the products page."""
        self.click_button(*CheckoutCmpltPageLocators.BACKHOME_BTN)

    def check_privacy_link(self):
        """Check that the privacy link is present on the page
        and that it can be clicked to navigate to the privacy policy page."""
        assert self.element_is_present(
            *PageLocators.ROBOT_IMG
        ), "The footer_robot is not present on the page"
        self.browser.find_element(*PageLocators.PRIVACY).click()
