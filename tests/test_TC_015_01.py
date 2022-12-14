# -*- coding: utf-8 -*-
# @Time    : 2022/11/22 10:00
# @Author  : Alexander Tomelo
import pytest
import allure
from src.src import (
    LoginPageSrc,
    ProductsPageSrc,
    CartPageSrc,
)
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.sidebar import SideBar


class TestSample:
    def authorization(self, d, username, password):
        """Method for authorization user.

        Args:
            d:          WebDriver
            username:   name of current test user
            password:   password of current test user
        """

        # Creates the Authorization Page instance
        page = LoginPage(d, LoginPageSrc.URL)
        # Opens the Authorization Page
        page.open_page()
        # Checks that the current page is Authorization Page
        page.should_be_login_page()
        # User's authorization
        page.register_user(username, password)

    def preconditions(self, d, username, password):
        """Precondition execution method.

        Args:
            d:          WebDriver
            username:   name of current test user
            password:   password of current test user
        """
        self.authorization(d, username, password)

        # проверка, что в корзине ничего нет
        page = ProductsPage(d, ProductsPageSrc.URL)
        page.open_page()
        try:
            page.should_be_empty_shopping_cart_badge()
        except AssertionError:
            # go to cart page
            # Creates the Cart Page instance
            page = CartPage(d, CartPageSrc.URL)
            # Open cart page
            page.open_page()
            # Clear cart
            page.clear_cart()
            page = ProductsPage(d, ProductsPageSrc.URL)
            page.open_page()

    @allure.feature("US_015 | Save cart data current user")
    @allure.story("TC_016.01 | Save cart data of current user after re-login")
    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            # ("performance_glitch_user", "secret_sauce"),
            # ("problem_user", "secret_sauce"),
            # pytest.param(
            #     "locked_out_user",
            #     "secret_sauce",
            #     marks=pytest.mark.xfail(raises=AssertionError),
            # ),
        ],
    )
    def test_safe_cart_data_after_re_login(self, d, username, password):
        """Check save cart data of current user after re-login

        Args:
            d: WebDriver
            username: username
            password: password
        """
        # Test Data
        sel_item_name = "Test.allTheThings() T-Shirt (Red)"
        sel_item_qty = "1"
        sel_item_price = "$15.99"

        # Part Preconditions
        self.preconditions(d, username, password)

        # Part 1 of test
        page = ProductsPage(d, ProductsPageSrc.URL)

        # Checks that the current page is Products Page
        page.should_be_products_page()

        # Step 1 if TC - Add Test.allTheThings() T-Shirt (Red) into cart
        page.add_item_on_products_page(sel_item_name)

        # Step 2 of TC - Click to hamburger menu
        page = SideBar(d, ProductsPageSrc.URL)
        page.click_hamburger_menu()

        # Step 3-1 of TC - Click to "LOGOUT"
        page.click_logout()
        page = LoginPage(d, LoginPageSrc.URL)
        page.should_be_login_page()

        # Part 2 of test
        # Step 3-2 - Login
        # User's authorization
        self.authorization(d, username, password)

        # Step 4 - Press "Cart" icon on the page
        # go to the products page
        page = ProductsPage(d, ProductsPageSrc.URL)
        page.should_be_products_page()
        page.go_to_basket_page()

        # go to the cart page
        page = CartPage(d, CartPageSrc.URL)
        page.should_be_cart_page()

        # Expected result. Check that the selected item is in the cart
        page.check_product_name_in_cart(sel_item_name)
        page.check_the_item_quantity_in_cart(sel_item_name, sel_item_qty)
        page.check_the_item_price_in_cart(sel_item_name, sel_item_price)

        # Part Postconditions
        self.postconditions(d, username, password)

    def postconditions(self, d, username, password):
        """Postcondition execution method.

        Args:
            d: WebDriver
            username: name of current test user
            password: password of current test user
        """
        self.preconditions(d, username, password)
