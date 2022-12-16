# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 17:47
# @Author  : Rustam S

import allure
import conf
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators
from pages.locators import ProductsPageLocators


class TestAddToCartAllItems:
    @allure.feature("US_006 | Adding an item to the cart")
    @allure.story("TC_006_01 | Adding items to your non-empty cart")
    def test_TC_006_01_add_to_cart(self, d):
        assert d.current_url == conf.URL

        # login standard user
        d.find_element(*LoginPageLocators.INPUT_USERNAME).send_keys("standard_user")
        d.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys("secret_sauce")
        d.find_element(*LoginPageLocators.LOGIN_BTN).click()

        assert d.current_url == "https://www.saucedemo.com/inventory.html"

        inventory_list = d.find_elements(*ProductsPageLocators.INVENTORY_ITEM)

        for item in range(0, len(inventory_list)):
            item += 1
            add_to_cart_button = d.find_element(
                By.XPATH, f"(//button[contains(@class,'inventory')])[{item}]"
            )
            add_to_cart_button.click()
            cart_link = d.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
            cart_link.click()
            continue_shopping_button = d.find_element(
                By.CSS_SELECTOR, '[name="continue-shopping"]'
            )
            continue_shopping_button.click()

        shopping_cart = d.find_element(*ProductsPageLocators.SHOP_CART_LINK).text
        assert shopping_cart == "6"

    def test_remove_from_cart(self, d):
        shopping_cart = d.find_element(*ProductsPageLocators.SHOP_CART_LINK).text
        assert shopping_cart == "6"

        d.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        assert d.current_url == "https://www.saucedemo.com/cart.html"

        cart_item = d.find_elements(By.CSS_SELECTOR, ".cart_item")

        for item in range(0, len(cart_item)):
            remove_from_cart_button = d.find_element(By.CSS_SELECTOR, "[name*=remove]")
            remove_from_cart_button.click()

        shopping_cart = d.find_element(*ProductsPageLocators.SHOP_CART_LINK).text
        assert shopping_cart == ""
