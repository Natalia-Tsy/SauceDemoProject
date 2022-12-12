import pytest
from selenium.common.exceptions import InvalidSelectorException
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_1_page import CheckoutPage_1
from pages.checkout_2_page import CheckoutPage_2
from pages.checkout_cmplt_page import CheckouCmpltPage


class Tests:
    # TC_002.01 Read Privacy Policy from the catalog
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_check_privacy_catalog(self, d):
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)  # Creates the Products page instance
        page.should_be_products_page()  # Checks the current page is Progucts Page
        page.check_privacy_link()  # Tries to click on Privacy Policy

    # TC_002.002 Read Privacy Policy from the cart
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_check_privacy_cart(self, d):
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)  # Creates the Products page instance
        page.add_item_on_products_page(
            "Sauce Labs Onesie"
        )  # Adds one product into the cart
        page.go_to_basket_page()  # gets to the Cart page
        link = "https://www.saucedemo.com/cart.html"
        page = CartPage(d, link)  # Creates the Cart page instance
        page.check_privacy_link()  # tries to click on Privacy Policy

    # TC_002.03 Read Privacy Policy from the checkout page
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_check_privacy_checkout1(self, d):
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)  # Creates the Products page instance
        page.add_item_on_products_page(
            "Sauce Labs Onesie"
        )  # Adds one product into the cart
        page.go_to_basket_page()  # Gets to the cart page
        link = "https://www.saucedemo.com/cart.html"
        page = CartPage(d, link)  # Creates the Cart Page instance
        page.go_to_checkout_1_page()  # gets to Checkout-one page
        link = "https://www.saucedemo.com/checkout-step-one.html"
        page = CheckoutPage_1(d, link)  # Creates the Checkout-one instance
        page.should_be_checkout_1_page()  # Checks the current page is Checkout-1 page
        page.set_shipping_info("John", "Smith", "33009")  # Enters shipping data
        page.go_to_checkout_2_page()  # Gets to Checkput-two page
        page.check_privacy_link()  # Tries to click on Privacy Policy

    # TC_002.04 Read Privacy Policy from the checkout overview page
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_check_privacy_checkout2(self, d):
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)  # Creates the Products page instance
        page.add_item_on_products_page(
            "Sauce Labs Onesie"
        )  # Adds one product into the cart
        page.go_to_basket_page()  # Gets to the cart page
        link = "https://www.saucedemo.com/cart.html"
        page = CartPage(d, link)  # Creates the Cart Page instance
        page.go_to_checkout_1_page()  # gets to Checkout-one page
        link = "https://www.saucedemo.com/checkout-step-one.html"
        page = CheckoutPage_1(d, link)  # Creates the Checkout-one instance
        page.should_be_checkout_1_page()  # Checks the current page is Checkout-1 page
        page.set_shipping_info("John", "Smith", "33009")  # Enters shipping data
        page.go_to_checkout_2_page()  # Gets to Checkput-two page
        link = "https://www.saucedemo.com/checkout-step-two.html"
        page = CheckoutPage_2(d, link)  # Creates the Checkout-two page instance
        page.should_be_checkout_2_page()  # Checks the current page is Checkout-2 page
        page.check_privacy_link()  # Tries to click on Privacy Policy

    # TC_002.05 Read Privacy Policy from the final Page
    @pytest.mark.xfail(raises=InvalidSelectorException)
    def test_check_privacy_checkout_complete(self, d):
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)  # Creates the ProductsPage instance
        page.add_item_on_products_page(
            "Sauce Labs Onesie"
        )  # puts one product into the cart
        page.go_to_basket_page()  # gets to the cart page
        link = "https://www.saucedemo.com/cart.html"
        page = CartPage(d, link)  # Creates the Cart Page instance
        page.go_to_checkout_1_page()  # gets to Checkout step 1 page
        link = "https://www.saucedemo.com/checkout-step-one.html"
        page = CheckoutPage_1(d, link)  # Creates the Checkout-one page instance
        page.should_be_checkout_1_page()  # Checks that the current page is Checkput-1 page
        page.set_shipping_info("John", "Smith", "33009")  # Enters shipping data
        page.go_to_checkout_2_page()  # gets to checkout-2 page
        link = "https://www.saucedemo.com/checkout-step-two.html"
        page = CheckoutPage_2(d, link)  # Creates the Checkout-two instance
        page.should_be_checkout_2_page()  # Checks that the current page is Checkout-2 page
        page.go_to_checkout_complete_page()  # gets to the final page
        page = "https://www.saucedemo.com/checkout-complete.html"
        page = CheckouCmpltPage(d, link)  # Creates the Checkout-complete page instance
        page.should_be_checkout_complete_page()  # Checks the current page is Checkout-complete page
        page.check_privacy_link()  # tries to click on Privacy Policy
