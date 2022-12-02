from .base_page import BasePage
from .locators import Chckout2PageLocators
from .src import Chckout2PageSrc
from .locators import PageLocators


class CheckoutPage_2(BasePage):
    """
    Checks that the current page is Checkout-2 page
    """

    def should_be_checkout_2_page(self):
        """
        Checks that the current page meets the requirements
        Returns:
        """
        self.should_be_link(Chckout2PageSrc.LINK)
        # Checks that the text of page title element meets the requirements
        self.should_be_page_title(Chckout2PageSrc.TITLE, *Chckout2PageLocators.TITLE)
        self.should_be_btn_to_checkout_complete_page()

    # Checks that there's FINISH button on thr page

    def should_be_btn_to_checkout_complete_page(self):
        assert self.element_is_visible(Chckout2PageLocators.FINISH_BTN)

    # Goes to Checkout-complete page
    def go_to_checkout_complete_page(self):
        self.click_button(*Chckout2PageLocators.FINISH_BTN)

    # Checks the link Privacy Policy
    def check_privacy_link(self):
        assert self.element_is_present(*PageLocators.ROBOT_IMG), "something went wrong"
        self.browser.find_element(*PageLocators.PRIVACY).click()
