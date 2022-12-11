import pytest
from selenium.common import NoSuchElementException
from pages.locators import ProductsPageLocators
from pages.cart_page import CartPage
from conf import URL


class TestCartPage:
    @pytest.mark.parametrize(
        "username, password, products",
        [
            (
                "standard_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
            ),
            (
                "performance_glitch_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
            ),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
                marks=pytest.mark.xfail(
                    raises=(AssertionError, NoSuchElementException)
                ),
            ),
            pytest.param(
                "problem_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_add_products_in_basket_from_main_page(
        self, d, username, password, products
    ):
        """The test of checking the correspondence of the number of products on the cart page and on the basket icon on
        the main page"""
        page = CartPage(d, URL)
        # Opens the authorization page
        page.open_page()
        # User Registration
        page.register_user(username, password)
        # Adding products from the main page
        page.put_or_del_products_in_packet(products)
        # Removing products from the main page
        page.put_or_del_products_in_packet(products)
        # Getting the number of products from the basket icon
        num_products_after_add_in_basket = (
            page.view_and_remember_the_number_product_on_icon_basket()
        )
        # Getting data from the cart page and comparing the number of products displayed in the cart and on\
        # the cart icon
        page.get_data_about_products_in_basket(num_products_after_add_in_basket)
        # Removing all items from the shopping cart
        page.clear_cart()

    @pytest.mark.parametrize(
        "username, password, products",
        [
            (
                "standard_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
            ),
            (
                "performance_glitch_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
            ),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
                marks=pytest.mark.xfail(
                    raises=(AssertionError, NoSuchElementException)
                ),
            ),
            pytest.param(
                "problem_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_add_products_in_basket_from_product_card_page(
        self, d, username, password, products
    ):
        """Test to check the possibility of adding and removing an item from the product card"""
        list_del_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Test.allTheThings() T-Shirt (Red)",
        ]
        page = CartPage(d, URL)
        # Opens the authorization page
        page.open_page()
        # User Registration
        page.register_user(username, password)
        # Go to the product card and add the product to the cart
        page.get_ids_and_put_or_del_products_in_packet_on_the_card_page(products)
        # Go to the product card and delete products from the list_del_items list from the basket
        page.get_ids_and_put_or_del_products_in_packet_on_the_card_page(list_del_items)
        # Getting the number of products from the basket icon
        num_products_after_add_in_basket = (
            page.view_and_remember_the_number_product_on_icon_basket()
        )
        # Getting data from the cart page and comparing the number of products displayed in the cart and on \
        # the cart icon
        page.get_data_about_products_in_basket(num_products_after_add_in_basket)
        # Comparison of the product name in the shopping cart
        page.product_params_comparison_in_basket()
        # Removing all items from the shopping cart
        page.clear_cart()

    @pytest.mark.parametrize(
        "username, password, products",
        [
            (
                "standard_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
            ),
            (
                "performance_glitch_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
            ),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
                marks=pytest.mark.xfail(
                    raises=(AssertionError, NoSuchElementException)
                ),
            ),
            pytest.param(
                "problem_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_name_comparison_and_add_products_in_basket_from_product_card_page(
        self, d, username, password, products
    ):
        """A test to check the possibility of adding a product from the product card and comparing the added products to
        the cart by name and price"""
        page = CartPage(d, URL)
        # Opens the authorization page
        page.open_page()
        # User Registration
        page.register_user(username, password)
        # Go to the product card and add the product to the cart
        page.get_ids_and_put_or_del_products_in_packet_on_the_card_page(products)
        # Getting the number of products from the basket icon
        num_products_after_add_in_basket = (
            page.view_and_remember_the_number_product_on_icon_basket()
        )
        page.get_data_about_products_in_basket(num_products_after_add_in_basket)
        # Comparison of the product name in the shopping cart
        page.product_params_comparison_in_basket()
        # Removing all items from the shopping cart
        page.clear_cart()

    @pytest.mark.parametrize(
        "username, password, products",
        [
            (
                "standard_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
            ),
            (
                "performance_glitch_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
            ),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
                marks=pytest.mark.xfail(
                    raises=(AssertionError, NoSuchElementException)
                ),
            ),
            pytest.param(
                "problem_user",
                "secret_sauce",
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Fleece Jacket",
                    "Test.allTheThings() T-Shirt (Red)",
                ],
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_del_all_product_in_basket_page(self, d, username, password, products):
        """Test to check whether it is possible to delete all products from the basket"""
        page = CartPage(d, URL)
        # Opens the authorization page
        page.open_page()
        # User Registration
        page.register_user(username, password)
        # Adding products from the main page
        page.put_or_del_products_in_packet(products)
        # Go to the shopping cart
        page.click_button(*ProductsPageLocators.SHOP_CART_LINK)
        # Clearing the basket of goods
        page.clear_cart()
        # Checking that all products have been removed from the cart
        page.check_number_products_in_basket_is_zero()
