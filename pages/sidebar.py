from .base_page import BasePage
from .locators import SideBarLocator


class SideBar(BasePage):
    """This class is used to test the functionality of the side bar of the website.

    Args:
        BasePage: Contains common methods that are used by all page classes
    """
    def click_hamburger_menu(self):
        """Open the hamburger menu, allowing the user to access the options it contains."""        
        self.element_is_visible(SideBarLocator.HAMBURGER)
        self.browser.find_element(*SideBarLocator.HAMBURGER).click()

    def click_logout(self):
        """Click the logout button in the side bar of the page."""
        self.element_is_visible(SideBarLocator.LOGOUT)
        self.browser.find_element(*SideBarLocator.LOGOUT).click()
