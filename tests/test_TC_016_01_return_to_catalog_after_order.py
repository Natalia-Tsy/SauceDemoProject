# -*- coding: utf-8 -*-
# @Time    : 2022/11/22 16:55
# @Author  : OlegKomissarovV
import pytest
import allure
from src.src import (
    LoginPageSrc,
    ProductsPageSrc,
    CartPageSrc,
    CheckoutCmpltPageSrc,
    Chckout2PageSrc,
    Chckout1PageSrc,
)
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.checkout_1_page import CheckoutPage_1
from pages.checkout_2_page import CheckoutPage_2
from pages.checkout_cmplt_page import CheckouCmpltPage


class TestSample:
    def test_user_can_go_to_login_page(self, d):
        """Checks whether a user can navigate to the login page of a website.

        Args:
            d: WebDriver
        """
        page = LoginPage(d, LoginPageSrc.URL)
        page.open_page()
        page.should_be_login_page()

    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_user_can_go_to_products_page(self, d, username, password):
        """Checks whether a user can navigate to the products page of a website after logging in.

        Args:
            d: WebDriver
            username: used to specify the username of the user
            password: used to specify the password of the user
        """
        self.test_user_can_go_to_login_page(d)
        page = LoginPage(d, LoginPageSrc.URL)
        page.register_user(username, password)
        page = ProductsPage(d, ProductsPageSrc.URL)
        page.should_be_products_page()

    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_user_can_go_to_cart_page(self, d, username, password):
        """Checks whether a user can navigate to the cart page of a website after logging in and adding items to cart.

        Args:
            d: WebDriver
            username: used to specify the username of the user
            password: used to specify the password of the user
        """
        self.test_user_can_go_to_products_page(d, username, password)
        page = ProductsPage(d, ProductsPageSrc.URL)
        page.add_item_on_products_page("Sauce Labs Onesie", "Sauce Labs Backpack")
        page.go_to_basket_page()
        page = CartPage(d, CartPageSrc.URL)
        page.should_be_cart_page()

    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_user_can_go_to_checkout_1_page(self, d, username, password):
        """Checks whether a user can navigate to the first checkout page of a website
        after logging in, adding items to cart, and navigating to the cart page.

        Args:
            d: WebDriver
            username: used to specify the username of the user
            password: used to specify the password of the user
        """
        self.test_user_can_go_to_cart_page(d, username, password)
        page = CartPage(d, CartPageSrc.URL)
        page.go_to_checkout_1_page()
        page = CheckoutPage_1(d, Chckout1PageSrc.URL)
        page.should_be_checkout_1_page()

    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            pytest.param(
                "problem_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_user_can_go_to_checkout_2_page(self, d, username, password):
        """Checks whether a user can navigate to the second checkout page of a website
        after logging in, adding items to cart, navigating to the cart page,
        and filling out the shipping information on the first checkout page.

        Args:
            d: WebDriver
            username: used to specify the username of the user
            password: used to specify the password of the user
        """
        self.test_user_can_go_to_checkout_1_page(d, username, password)
        page = CheckoutPage_1(d, Chckout1PageSrc.URL)
        page.set_shipping_info("John", "Smith", "33009")
        page.go_to_checkout_2_page()
        page = CheckoutPage_2(d, Chckout2PageSrc.URL)
        page.should_be_checkout_2_page()

    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            pytest.param(
                "problem_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_user_can_go_to_checkout_complete_page(self, d, username, password):
        """Checks whether a user can navigate to the checkout complete page of a website
        after logging in, adding items to cart, navigating to the cart page,
        filling out the shipping information on the first checkout page, and navigating to the second checkout page.

        Args:
            d: WebDriver
            username: used to specify the username of the user
            password: used to specify the password of the user
        """
        self.test_user_can_go_to_checkout_2_page(d, username, password)
        page = CheckoutPage_2(d, Chckout2PageSrc.URL)
        page.go_to_checkout_complete_page()
        page = CheckouCmpltPage(d, CheckoutCmpltPageSrc.URL)
        page.should_be_checkout_complete_page()

    @allure.feature("US_016 | Return to the products page")
    @allure.story("TC_016.01 | Return to products page from checkout complete page")
    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            pytest.param(
                "problem_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_TC_016_01_return_to_catalog_after_order(self, d, username, password):
        """Checks whether a user can return to the products page of a website
        after completing an order and verifying that the cart is empty

        Args:
            d: WebDriver
            username: used to specify the username of the user
            password: used to specify the password of the user
        """
        self.test_user_can_go_to_checkout_complete_page(d, username, password)
        page = CheckouCmpltPage(d, CheckoutCmpltPageSrc.URL)
        page.go_to_products_page()
        page = ProductsPage(d, ProductsPageSrc.URL)
        page.should_be_products_page()
        page.should_be_empty_shopping_cart_badge()
