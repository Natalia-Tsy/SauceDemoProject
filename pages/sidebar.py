from .base_page import BasePage
from .locators import SideBarLocator


class SideBar(BasePage):
    """This class is used to test the functionality of the sidebar on products page.

    Args:
        BasePage: Contains common methods that are used by all page classes
    """

    def click_hamburger_menu(self):
        """Check that hamburger menu on the current page is visible and open it."""
        self.element_is_visible(SideBarLocator.HAMBURGER)
        self.browser.find_element(*SideBarLocator.HAMBURGER).click()

    def click_logout(self):
        """Check that LOGOUT item is visible in hamburger menu and click it."""
        self.element_is_visible(SideBarLocator.LOGOUT)
        self.browser.find_element(*SideBarLocator.LOGOUT).click()
