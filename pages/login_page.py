from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators
from .src import LoginPageSrc


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_link(LoginPageSrc.LINK)
        # Checks there's an element to input the User's first name on the current page
        assert self.element_is_present(*LoginPageLocators.INPUT_USERNAME)
        # Checks there's an element to input the Password on the current page
        assert self.element_is_present(*LoginPageLocators.INPUT_PASSWORD)
        # Checks there's an element to confirm authorization on the current page
        assert self.element_is_present(*LoginPageLocators.LOGIN_BTN)
        # # Checks there are Users' names on the current page
        # assert self.element_is_present(*LoginPageLocators.LOGIN_CREDENTIALS)
        # # Checks there are Users' the passwords on the current page
        # assert self.element_is_present(*LoginPageLocators.LOGIN_PASSWORD)

    def register_user(self, username, password):
        # n = 1
        # h = self.get_text(n, *LoginPageLocators.LOGIN_CREDENTIALS)
        # w = self.get_text(n, *LoginPageLocators.LOGIN_PASSWORD)
        # User's name is passed to the text element on the login page
        self.browser.find_element(*LoginPageLocators.INPUT_USERNAME).send_keys(username)
        # Password is passed to the text element on the login page
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        # "LOGIN" button is pressed
        self.click_button(*LoginPageLocators.LOGIN_BTN)

    def should_be_error_message(self):
        # Checks there's Error message on the current page
        btn_error = self.browser.find_element(*LoginPageLocators.ERROR_BTN)
        assert btn_error.text == LoginPageSrc.ERROR_BTN_TEXT, "wrong test"

    # Inputs the data to log in
    def user_can_authorize(self):
        self.browser.find_element(By.ID, "user-name").send_keys("standard_user")
        self.browser.find_element(By.XPATH, "//input[@id='password']").send_keys(
            "secret_sauce"
        )
        self.browser.find_element(By.XPATH, "//input[@name='login-button']").click()
