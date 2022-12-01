import pytest
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.checkout_1_page import CheckoutPage_1
from pages.checkout_2_page import CheckoutPage_2
from pages.checkout_cmplt_page import CheckouCmpltPage

link = "https://www.saucedemo.com/"


class TestSample:
    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("locked_out_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            ("problem_user", "secret_sauce"),
        ],
    )
    # The test checks that the User can perform user's authorization
    def test_register_user(self, d, username, password):

        # Creates the Authorization Page instance
        page = LoginPage(d, link)
        # Opens the Authorization Page
        page.open_page()
        # Checks that the current page is Authorization Page
        page.should_be_login_page()
        # User's authorization
        page.register_user(username, password)

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
    # The test checks that the user can get to the Product Page
    # from Authorization Page
    def test_user_can_go_to_products_page(self, d, username, password):
        # User's authorization
        self.test_register_user(d, username, password)
        # if Users == ("locked_out_user", "secret_sauce"):
        #     pytest.xfail()
        link = "https://www.saucedemo.com/inventory.html"
        # Creates the Product Page instance
        page = ProductsPage(d, link)
        # Checks that the current page is Products Page
        page.should_be_products_page()
        # Products that were selected by name
        # are added to/removed from the cart
        # and the list of these products is returned
        page.add_item_on_products_page("Sauce Labs Onesie", "Sauce Labs Backpack")
        # Gets to the Cart Page
        page.go_to_basket_page()

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
    # The test checks that the user can get to the Product Page
    # from Authorization Page
    def test_user_can_go_to_cart_page(self, d, username, password):
        self.test_user_can_go_to_products_page(d, username, password)
        link = "https://www.saucedemo.com/cart.html"
        # Creates the Cart Page instance
        page = CartPage(d, link)
        # Checks the current page is Cart Page
        page.should_be_cart_page()
        # Gets to the Checkout Page
        page.go_to_checkout_1_page()
        link = "https://www.saucedemo.com/checkout-step-one.html"
        # Creates the Checkout-1 Page instance
        page = CheckoutPage_1(d, link)
        # Checks that the current page is Checkout-1 Page
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
    # The test checks that the user can get to the Product Page
    # from Authorization Page
    def test_user_can_go_to_checkout_1_page(self, d, username, password):
        self.test_user_can_go_to_cart_page(d, username, password)
        link = "https://www.saucedemo.com/checkout-step-one.html"
        # Creates the Checkout-1 page instance
        page = CheckoutPage_1(d, link)
        # Checks the current page is Checkout-1 page
        page.should_be_checkout_1_page()
        # The data that is required to receive the product is filled
        page.set_shipping_info("John", "Smith", "33009")
        # Gets to the next page of Checkout (Checkout-2)
        page.go_to_checkout_2_page()
        link = "https://www.saucedemo.com/checkout-step-two.html"
        # Creates the Checkout-2 instance
        page = CheckoutPage_2(d, link)
        # Checks the current page is Checkout-2 page
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
    def test_user_can_go_to_checkout_2_page(self, d, username, password):
        self.test_user_can_go_to_checkout_1_page(d, username, password)
        link = "https://www.saucedemo.com/checkout-step-two.html"
        # Creates the Checkout-2 Page instance
        page = CheckoutPage_2(d, link)
        # Checks the vurrent page is Checkout-2 page
        page.should_be_checkout_2_page()
        # Gets to the Checkout-complete page
        page.go_to_checkout_complete_page()
        link = "https://www.saucedemo.com/checkout-complete.html"
        # Creates the Checkout-complete page instance
        page = CheckouCmpltPage(d, link)
        # Checks the current page is Checkout-complete page
        page.should_be_checkout_complete_page()

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
        self.test_user_can_go_to_checkout_2_page(d, username, password)
        link = "https://www.saucedemo.com/checkout-complete.html"
        # Creates the Checkout-complete Page instance
        page = CheckouCmpltPage(d, link)
        # Checks the current page is Checkout-complete Page
        page.should_be_checkout_complete_page()
        # Gets to the Products page
        page.go_to_products_page()
        link = "https://www.saucedemo.com/inventory.html"
        # Creates the Products Page instance
        page = ProductsPage(d, link)
        # Checks the current page is Products Page
        page.should_be_products_page()
        # Checks the Cart icon on the current page doesn't display any products
        page.should_be_empty_shopping_cart_badge()
