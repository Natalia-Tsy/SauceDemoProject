from .base_page import BasePage
from .locators import PageLocators, Chckout1PageLocators
from src.src import Chckout1PageSrc


class CheckoutPage_1(BasePage):
    """This class is used to test the functionality of the first checkout page of the website.

    Args:
        BasePage: Contains common methods that are used by all page classes
    """

    def should_be_checkout_1_page(self):
        """Check that the current page is the first checkout page."""
        self.should_be_link(Chckout1PageSrc.LINK)
        self.should_be_page_title(Chckout1PageSrc.TITLE, *Chckout1PageLocators.TITLE)
        self.should_be_input_firstname_to_checkout_1_page()
        self.should_be_input_lastname_to_checkout_1_page()
        self.should_be_input_postal_code_to_checkout_1_page()
        self.should_be_btn_to_checkout_1_page()

    def should_be_input_firstname_to_checkout_1_page(self):
        """Check the first name input field is present on the page."""
        assert self.element_is_present(
            *Chckout1PageLocators.INPUT_FIRSTNAME
        ), "The first name input field is not present on the page"

    def should_be_input_lastname_to_checkout_1_page(self):
        """Check the last name input field is present on the page."""
        assert self.element_is_present(
            *Chckout1PageLocators.INPUT_LASTNAME
        ), "The last name input field is not present on the page"

    def should_be_input_postal_code_to_checkout_1_page(self):
        """Check the postal code input field is present on the page."""
        assert self.element_is_present(
            *Chckout1PageLocators.INPUT_CODE
        ), "The postal code input field is not present on the page"

    def should_be_btn_to_checkout_1_page(self):
        """Check the "CONTINUE" button is visible on the page."""
        assert self.element_is_visible(
            Chckout1PageLocators.CONTINUE_BTN
        ), "The continue button is not visible on the page"

    def set_shipping_info(self, firstname, lastname, code):
        """Set the shipping information on the first checkout page

        Args:
            firstname: first name user
            lastname: last name user
            code: postal code
        """
        # User's first name is passed to the text element on the page
        self.browser.find_element(*Chckout1PageLocators.INPUT_FIRSTNAME).send_keys(
            firstname
        )
        # User's last name is passed to the text element on the page
        self.browser.find_element(*Chckout1PageLocators.INPUT_LASTNAME).send_keys(
            lastname
        )
        # User's zipcode is passed to the text element on the page
        self.browser.find_element(*Chckout1PageLocators.INPUT_CODE).send_keys(code)

    def go_to_checkout_2_page(self):
        """Navigate to the second checkout page."""
        self.click_button(*Chckout1PageLocators.CONTINUE_BTN)

    def check_privacy_link(self):
        """Check that the privacy link is present on the page
        and that it can be clicked to navigate to the privacy policy page."""
        assert self.element_is_present(
            *PageLocators.ROBOT_IMG
        ), "The footer_robot is not present on the page"
        self.browser.find_element(*PageLocators.PRIVACY).click()
