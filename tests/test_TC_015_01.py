import pytest
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.sidebar import SideBar


class TestSample:
    # авторизация пользователя
    def to_do_registration(self, d, username, password):
        link = "https://www.saucedemo.com/"
        # Creates the Authorization Page instance
        page = LoginPage(d, link)
        # Opens the Authorization Page
        page.open_page()
        # Checks that the current page is Authorization Page
        page.should_be_login_page()
        # User's authorization
        page.register_user(username, password)

    # Метод проверки выполнения предусловий, при необходимости, их обеспечения:
    # 1. проверяет, что корзина пуста
    # 2. если нет, то удаляет из корзины все товары
    def preconditions(self, d, username, password):
        # autorization
        self.to_do_registration(d, username, password)
        # проверка, что в корзине ничего нет
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)
        page.open_page()
        try:
            page.should_be_empty_shopping_cart_badge()
        except AssertionError:
            # go to cart page
            link = "https://www.saucedemo.com/cart.html"
            # Creates the Cart Page instance
            page = CartPage(d, link)
            # Open cart page
            page.open_page()
            # Clear cart
            page.clear_cart()
        finally:
            link = "https://www.saucedemo.com/inventory.html"
            page = ProductsPage(d, link)
            page.open_page()

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
    # Тест сохранности заполненной корзины  после перелогинивания
    def test_safe_cart_data_after_re_login(self, d, username, password):
        # Test Data
        sel_item_name = "Test.allTheThings() T-Shirt (Red)"
        sel_item_qty = "1"
        sel_item_price = "$15.99"
        # Part Preconditions
        self.preconditions(d, username, password)

        # Part 1 of test
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)
        page.open_page()
        # Checks that the current page is Products Page
        page.should_be_products_page()

        # Step 1 if TC - Add Test.allTheThings() T-Shirt (Red) into cart
        page.add_item_on_products_page(sel_item_name)

        # Step 2 of TC - Click to hamburger menu
        page = SideBar(d, link)
        page.click_hamburger_menu()

        # Step 3-1 of TC - Click to "LOGOUT"
        page.click_logout_from_top_left_menu()
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)
        page.should_be_login_page()

        # Part 2 of test
        # Step 3-2 - Login
        # User's authorization
        self.to_do_registration(d, username, password)

        # Step 4 - Press "Cart" icon on the page
        # go to the cart page
        link = "https://www.saucedemo.com/cart.html"
        page = CartPage(d, link)
        page.open_page()
        page.should_be_cart_page()

        # Expected result. Check that the selected item is in the cart
        page.check_this_item_is_presents_in_the_cart(
            sel_item_name, sel_item_qty, sel_item_price
        )

        # Part Postconditions
        self.postconditions(d, username, password)

    # Модуль выполнения постусловий:
    # 1. проверяет, что корзина пуста
    # 2. если нет, то удаляет из корзины все товары
    def postconditions(self, d, username, password):
        self.preconditions(d, username, password)
