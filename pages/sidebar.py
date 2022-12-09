from .base_page import BasePage
from .locators import SideBarLocator


class SideBar(BasePage):

    # Opens hamburger menu
    def click_hamburger_menu(self):
        self.element_is_visible(SideBarLocator.HAMBURGER)
        self.browser.find_element(*SideBarLocator.HAMBURGER).click()

    # Select and click LOGOUT item from hamburger menu
    def click_logout(self):
        self.element_is_visible(SideBarLocator.LOGOUT)
        self.browser.find_element(*SideBarLocator.LOGOUT).click()
