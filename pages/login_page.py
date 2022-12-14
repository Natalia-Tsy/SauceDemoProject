from .base_page import BasePage
from .locators import LoginPageLocators
from src.src import LoginPageSrc


class LoginPage(BasePage):
    """This class is used to test the functionality of the login page of the website.

    Args:
        BasePage: Contains common methods that are used by all page classes
    """

    def should_be_login_page(self):
        """Check that the current page is the login page"""
        self.should_be_link(LoginPageSrc.URL)
        assert self.element_is_present(
            *LoginPageLocators.INPUT_USERNAME
        ), "The username input field is not present on the page"
        assert self.element_is_present(
            *LoginPageLocators.INPUT_PASSWORD
        ), "The password input field is not present on the page"
        assert self.element_is_visible(
            LoginPageLocators.LOGIN_BTN
        ), "The login button is not visible on the page"

    def register_user(self, username, password):
        """Register user on the login page.

        Args:
            username: username user
            password: password user
        """
        # User's name is passed to the text element on the login page
        self.browser.find_element(*LoginPageLocators.INPUT_USERNAME).send_keys(username)
        # Password is passed to the text element on the login page
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        # "LOGIN" button is pressed
        self.click_button(*LoginPageLocators.LOGIN_BTN)

    def should_be_error_message(self):
        """Check an error message is displayed on the page and that the error message text is correct."""
        btn_error = self.browser.find_element(*LoginPageLocators.ERROR_BTN)
        assert (
            btn_error.text == LoginPageSrc.ERROR_BTN_TEXT
        ), "The error message displayed on the page does not match the expected text"
