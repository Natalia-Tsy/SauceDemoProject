import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProductsPageLocators, CardProductPageLocator


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    # Opens a page
    def open_page(self):
        self.browser.get(self.link)

    # Object WebElement is returned in
    # accordance with the specified search criteria
    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    # WebElements list, meeting the search requirements, is returned
    def elements_are_present(self, method, locator):
        try:
            return self.browser.find_elements(method, locator)
        except NoSuchElementException:
            return NoSuchElementException

    # Either returns the element or sets up waiting timeout seconds
    # until the object appears
    # before TimeOutException arises
    # if the element doesn't appear during timeout
    def element_is_visible(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    # Either returns the elements or sets up timeout
    # seconds until the exception TimeoutException is returned
    # if the element doesn't appear during timeout
    #
    def elements_are_located(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(
            EC.presence_of_all_elements_located((locator))
        )

    # Either returns the elements or sets up timeout
    #     seconds until the exception TimeoutException is returned
    #     if the element doesn't appear during timeout
    def element_is_located(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(
            EC.presence_of_element_located((locator))
        )

    def element_is_located_in_element(self, element, locator, timeout=5):
        return Wait(element, timeout).until(EC.presence_of_element_located((locator)))

    # Проверяет, что текущая страница соответствует требованиям
    def should_be_link(self, link):
        assert link in self.browser.current_url, "wrong url"

    # Checks that the texts of page title element meets the requirements
    def should_be_page_title(self, title, method, locator):
        el_title = self.browser.find_element(method, locator)
        # Gets the page title element
        assert el_title, "there is no title"
        # Checks that the page title element meets the requirements
        assert title == el_title.text, "wrong title"

    # Return the elements text that meets
    # the requirements from the specified index i
    def get_text(self, i, method, locator):
        return self.browser.find_element(method, locator).text.split("\n")[i:]

    #  Unpacks the list of elements list into element list
    def flatten(self, mylist):
        return [item for sublist in mylist for item in sublist]

    # The button is pressed on the locator
    def click_button(self, method, locator):
        self.browser.find_element(method, locator).click()

    # Метод получения количества товаров в корзине
    def get_num_products_in_basket(self, method, locator):
        try:
            return self.browser.find_elements(method, locator)
        except NoSuchElementException:
            return []

    # Метод получения ID товара
    def get_id_product(self, element):
        product_id = (
            element.find_element(*ProductsPageLocators.PRODUCT_ID)
            .get_attribute("id")
            .split("_title_link")[0]
            .split("item_")[1]
        )
        return product_id

    # Метод добавления/удаления товаров с/из карточки товара в/из корзину(ы)
    def add_or_del_product_from_card_product_page(self, product_id, name_product):
        url = f"https://www.saucedemo.com/inventory-item.html?id={product_id}"
        self.browser.get(url)
        time.sleep(1)
        name_product_from_card_page = self.browser.find_element(
            *CardProductPageLocator.NAME_PRODUCT
        ).text
        if name_product_from_card_page in name_product:
            try:
                self.browser.find_element(*CardProductPageLocator.ADD_BTN).click()
            except NoSuchElementException:
                self.browser.find_element(*CardProductPageLocator.DEL_BTN).click()
            self.browser.find_element(
                *CardProductPageLocator.BACK_TO_THE_MAIN_PAGE_BTN
            ).click()

    # Метод очистки знака доллара в цене товара
    def clearing_characters(self, char, data):
        return data.replace(char, "")
