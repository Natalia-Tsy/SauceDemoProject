# -*- coding: utf-8 -*-
# @Time    : 2022/12/12 19:00
# @Author  : Natalia Ts

import allure
from selenium.common import NoSuchElementException
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest
from src.src import LoginPageSrc, ProductsPageSrc, CartPageSrc


class Tests:
    @allure.feature("US_014 | Exit to the catalog of products from the cart in order")
    @allure.story(
        "TC_014.02 | Return to the catalog of products from shopping cart using the menu item ALL ITEMS"
    )
    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            pytest.param(
                "problem_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=NoSuchElementException),
            ),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_return_to_the_catalog_all_items(self, d, username, password):
        page = LoginPage(d, LoginPageSrc.URL)  # Creates the Login page instance
        page.open_page()
        page.register_user(username, password)  # user logs in
        page = ProductsPage(
            d, ProductsPageSrc.URL
        )  # Creates the Products page instance
        page.should_be_products_page()
        page.add_item_on_products_page(
            "Sauce Labs Fleece Jacket", "Test.allTheThings() T-Shirt (Red)"
        )
        page.go_to_basket_page()  # gets to the Cart page
        page = CartPage(d, CartPageSrc.URL)
        page.check_the_quantity()  # checks the cart is not empty
        page.open_hamburger()
        page.click_all_items()
        page = ProductsPage(
            d, ProductsPageSrc.URL
        )  # creates the Products page instance
        page.should_be_products_page()  # Checks we're on the Product page
        page.go_to_basket_page()  # go to cart to remove the items (for the following users)
        page = CartPage(d, CartPageSrc.URL)
        page.clear_cart()
