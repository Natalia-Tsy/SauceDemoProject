# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 17:40
# @Author  : Rustam S

import conf
import allure
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators
from pages.locators import ProductsPageLocators


class TestAddRemoveAllItems:
    def test_add_all_to_cart(self, d):
        assert d.current_url == conf.URL

        # login
        d.find_element(*LoginPageLocators.INPUT_USERNAME).send_keys("standard_user")
        d.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys("secret_sauce")
        d.find_element(*LoginPageLocators.LOGIN_BTN).click()

        assert d.current_url == "https://www.saucedemo.com/inventory.html"

        inventory_list = d.find_elements(*ProductsPageLocators.INVENTORY_ITEM)

        for add_to_cart_button in inventory_list:
            add_to_cart_button = d.find_element(By.CSS_SELECTOR, "[name*=add-to-cart]")
            add_to_cart_button.click()

        shopping_cart = d.find_element(*ProductsPageLocators.SHOP_CART_LINK).text
        assert shopping_cart == "6"

    @allure.feature("US_011 | Removing an item from the cart")
    @allure.story("TC_011.07 Removing items from the cart")
    def test_TC_011_07_remove_all_from_cart(self, d):
        assert d.current_url == "https://www.saucedemo.com/inventory.html"

        shopping_cart = d.find_element(*ProductsPageLocators.SHOP_CART_LINK).text
        assert shopping_cart == "6"

        inventory_list = d.find_elements(*ProductsPageLocators.INVENTORY_ITEM)

        for remove_from_cart_button in inventory_list:
            remove_from_cart_button = d.find_element(By.CSS_SELECTOR, "[name*=remove]")
            remove_from_cart_button.click()

        shopping_cart = d.find_element(*ProductsPageLocators.SHOP_CART_LINK).text
        assert shopping_cart == ""
