import time

from selenium.webdriver.common.by import By
import conf
from pages.locators import LoginPageLocators
from pages.locators import ProductsPageLocators


class TestAddToCartAllItems:
    def test_add_to_cart(self, d):
        assert d.current_url == conf.URL

        # login
        d.find_element(*LoginPageLocators.INPUT_USERNAME).send_keys("standard_user")
        d.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys("secret_sauce")
        d.find_element(*LoginPageLocators.LOGIN_BTN).click()

        assert d.current_url == "https://www.saucedemo.com/inventory.html"

        inventory_list = d.find_elements(*ProductsPageLocators.INVENTORY_LIST)

        for item in range(0, len(inventory_list)):
            item += 1
            add_to_cart_button = d.find_element(
                By.XPATH, f"(//button[contains(@class,'inventory')])[{item}]"
            ).click()
            cart_link = d.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
            continue_shopping_button = d.find_element(
                By.CSS_SELECTOR, '[name="continue-shopping"]'
            ).click()

        shopping_cart = d.find_element(*ProductsPageLocators.SHOPPING_CART_LINK).text
        assert shopping_cart == "6"

    def test_remove_from_cart(self, d):
        shopping_cart = d.find_element(*ProductsPageLocators.SHOPPING_CART_LINK).text
        assert shopping_cart == "6"

        d.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        assert d.current_url == "https://www.saucedemo.com/cart.html"

        cart_item = d.find_elements(By.CSS_SELECTOR, ".cart_item")

        for item in range(0, len(cart_item)):
            remove_from_cart_button = d.find_element(
                By.CSS_SELECTOR, "[name*=remove]"
            ).click()

            # item += 1
            # add_to_cart_button = d.find_element(By.XPATH, f"(//button[contains(@class,'inventory')])[{item}]").click()
            # cart_link = d.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
            # continue_shopping_button = d.find_element(By.CSS_SELECTOR, '[name="continue-shopping"]').click()

        shopping_cart = d.find_element(*ProductsPageLocators.SHOPPING_CART_LINK).text
        assert shopping_cart == ""
