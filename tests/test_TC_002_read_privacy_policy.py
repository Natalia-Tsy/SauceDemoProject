# -*- coding: utf-8 -*-
# @Time    : 2022/3/12 10:00
# @Author  : Natalia Ts

import allure
import pytest
from selenium.common.exceptions import InvalidSelectorException
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_1_page import CheckoutPage_1
from pages.checkout_2_page import CheckoutPage_2
from pages.checkout_cmplt_page import CheckouCmpltPage
from src.src import (
    LoginPageSrc,
    ProductsPageSrc,
    CartPageSrc,
    CheckoutCmpltPageSrc,
    Chckout2PageSrc,
    Chckout1PageSrc,
)


class Tests:
    @allure.feature("US_002 | Privacy Policy")
    @allure.story("TC_002.01 | Read Privacy Policy from the catalog")
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_TC_002_01_read_privacy_policy_from_catalog(self, d):
        page = LoginPage(d, LoginPageSrc.URL)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        page = ProductsPage(
            d, ProductsPageSrc.URL
        )  # Creates the Products page instance
        page.should_be_products_page()  # Checks the current page is Progucts Page
        page.check_privacy_link()  # Tries to click on Privacy Policy

    @allure.feature("US_002 | Privacy Policy")
    @allure.story("TC_002.02 | Read Privacy Policy from the cart")
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_TC_002_02_read_privacy_policy_from_cart(self, d):
        page = LoginPage(d, LoginPageSrc.URL)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        page = ProductsPage(
            d, ProductsPageSrc.URL
        )  # Creates the Products page instance
        page.add_item_on_products_page(
            "Sauce Labs Onesie"
        )  # Adds one product into the cart
        page.go_to_basket_page()  # gets to the Cart page
        page = CartPage(d, CartPageSrc.URL)  # Creates the Cart page instance
        page.check_privacy_link()  # tries to click on Privacy Policy

    @allure.feature("US_002 | Privacy Policy")
    @allure.story("TC_002.03 | Read Privacy Policy from the checkout page")
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_TC_003_03_read_privacy_policy_from_checkout(self, d):
        page = LoginPage(d, LoginPageSrc.URL)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        page = ProductsPage(
            d, ProductsPageSrc.URL
        )  # Creates the Products page instance
        page.add_item_on_products_page(
            "Sauce Labs Onesie"
        )  # Adds one product into the cart
        page.go_to_basket_page()  # Gets to the cart page
        page = CartPage(d, CartPageSrc.URL)  # Creates the Cart Page instance
        page.go_to_checkout_1_page()  # gets to Checkout-one page
        page = CheckoutPage_1(
            d, Chckout1PageSrc.URL
        )  # Creates the Checkout-one instance
        page.should_be_checkout_1_page()  # Checks the current page is Checkout-1 page
        page.set_shipping_info("John", "Smith", "33009")  # Enters shipping data
        page.go_to_checkout_2_page()  # Gets to Checkout-two page
        page.check_privacy_link()  # Tries to click on Privacy Policy

    @allure.feature("US_002 | Privacy Policy")
    @allure.story("TC_002.04 | Read Privacy Policy from the checkout overview page")
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_TC_002_04_read_privacy_policy_from_checkout_overview(self, d):
        page = LoginPage(d, LoginPageSrc.URL)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        page = ProductsPage(
            d, ProductsPageSrc.URL
        )  # Creates the Products page instance
        page.add_item_on_products_page(
            "Sauce Labs Onesie"
        )  # Adds one product into the cart
        page.go_to_basket_page()  # Gets to the cart page
        page = CartPage(d, CartPageSrc.URL)  # Creates the Cart Page instance
        page.go_to_checkout_1_page()  # gets to Checkout-one page
        page = CheckoutPage_1(
            d, Chckout1PageSrc.URL
        )  # Creates the Checkout-one instance
        page.should_be_checkout_1_page()  # Checks the current page is Checkout-1 page
        page.set_shipping_info("John", "Smith", "33009")  # Enters shipping data
        page.go_to_checkout_2_page()  # Gets to Checkout-two page
        page = CheckoutPage_2(
            d, Chckout2PageSrc.URL
        )  # Creates the Checkout-two page instance
        page.should_be_checkout_2_page()  # Checks the current page is Checkout-2 page
        page.check_privacy_link()  # Tries to click on Privacy Policy

    @allure.feature("US_002 | Privacy Policy")
    @allure.story("TC_002.05 | Read Privacy Policy from the final page")
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_TC_002_05_read_privacy_policy_from_final_page(self, d):
        page = LoginPage(d, LoginPageSrc.URL)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        page = ProductsPage(d, ProductsPageSrc.URL)  # Creates the ProductsPage instance
        page.add_item_on_products_page(
            "Sauce Labs Onesie"
        )  # puts one product into the cart
        page.go_to_basket_page()  # gets to the cart page
        page = CartPage(d, CartPageSrc.URL)  # Creates the Cart Page instance
        page.go_to_checkout_1_page()  # gets to Checkout step 1 page
        page = CheckoutPage_1(
            d, Chckout1PageSrc.URL
        )  # Creates the Checkout-one page instance
        page.should_be_checkout_1_page()  # Checks that the current page is Checkout-1 page
        page.set_shipping_info("John", "Smith", "33009")  # Enters shipping data
        page.go_to_checkout_2_page()  # gets to checkout-2 page
        page = CheckoutPage_2(
            d, Chckout2PageSrc.URL
        )  # Creates the Checkout-two instance
        page.should_be_checkout_2_page()  # Checks that the current page is Checkout-2 page
        page.go_to_checkout_complete_page()  # gets to the final page
        page = CheckouCmpltPage(
            d, CheckoutCmpltPageSrc.URL
        )  # Creates the Checkout-complete page instance
        page.should_be_checkout_complete_page()  # Checks the current page is Checkout-complete page
        page.check_privacy_link()  # tries to click on Privacy Policy
