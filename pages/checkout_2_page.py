from .base_page import BasePage
from .locators import PageLocators, Chckout2PageLocators
from src.src import Chckout2PageSrc


class CheckoutPage_2(BasePage):
    """This class is used to test the functionality of the second checkout page of the website.

    Args:
        BasePage: Contains common methods that are used by all page classes
    """

    def should_be_checkout_2_page(self):
        """Check that the current page is the second checkout page."""
        self.should_be_link(Chckout2PageSrc.LINK)
        self.should_be_page_title(Chckout2PageSrc.TITLE, *Chckout2PageLocators.TITLE)
        self.should_be_btn_to_checkout_complete_page()

    def should_be_btn_to_checkout_complete_page(self):
        """Check the "FINISH" button is visible on the second checkout page."""
        assert self.element_is_visible(
            Chckout2PageLocators.FINISH_BTN
        ), "The finish button is not present or not visible on the page"

    def go_to_checkout_complete_page(self):
        """Navigate to the second checkout complete page."""
        self.click_button(*Chckout2PageLocators.FINISH_BTN)

    def check_privacy_link(self):
        """Check that the privacy link is present on the page
        and that it can be clicked to navigate to the privacy policy page."""
        assert self.element_is_present(
            *PageLocators.ROBOT_IMG
        ), "The footer_robot is not present on the page"
        self.browser.find_element(*PageLocators.PRIVACY).click()
