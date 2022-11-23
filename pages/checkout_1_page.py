from .base_page import BasePage
from .locators import Chckout1PageLocators
from .src import Chckout1PageSrc
from .locators import PageLocators


class CheckoutPage_1(BasePage):
    # Checks tha the current page is Checkout-1
    def should_be_checkout_1_page(self):
        # Checks that the current page meets the requirements
        self.should_be_link(Chckout1PageSrc.LINK)
        # Checks that the texts of the page title element meets the requirements
        self.should_be_page_title(Chckout1PageSrc.TITLE, *Chckout1PageLocators.TITLE)
        self.should_be_input_firstname_to_checkout_1_page()
        self.should_be_input_lastname_to_checkout_1_page()
        self.should_be_input_postal_code_to_checkout_1_page()
        self.should_be_btn_to_checkout_1_page()

        # Checks there's an element to input User's first name on the page

    def should_be_input_firstname_to_checkout_1_page(self):
        assert self.element_is_present(*Chckout1PageLocators.INPUT_FIRSTNAME)

        # Checks there's an element to input User's last name on the page

    def should_be_input_lastname_to_checkout_1_page(self):
        assert self.element_is_present(*Chckout1PageLocators.INPUT_LASTNAME)

        # Checks there's an element to input User's zipcode on the page

    def should_be_input_postal_code_to_checkout_1_page(self):
        assert self.element_is_present(*Chckout1PageLocators.INPUT_CODE)

    # Checks there's CHECKOUT button on the page
    def should_be_btn_to_checkout_1_page(self):
        assert self.element_is_visible(Chckout1PageLocators.CONTINUE_BTN)

    # The data required to receive the product is filled
    def set_shipping_info(self, firstname, lastname, code):
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

    # "CONTINUE" Button is pressed
    def go_to_checkout_2_page(self):
        self.click_button(*Chckout1PageLocators.CONTINUE_BTN)

    # Checks the link Privacy Policy
    def check_footer(self):
        assert self.element_is_present(*PageLocators.ROBOT), "something went wrong"
        self.browser.find_element(*PageLocators.PRIVACY).click()
