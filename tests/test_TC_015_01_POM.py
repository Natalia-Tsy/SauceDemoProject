import pytest

from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage


class TestSample:
    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            # ("locked_out_user", "secret_sauce"),
            # ("performance_glitch_user", "secret_sauce"),
            # ("problem_user", "secret_sauce"),
        ],
    )
    # Тест проверяет, что пользователь может выполнить авторизацию пользователя
    # The test checks that the User can perform user's authorization
    def test_register_user(self, d, username, password):
        link = "https://www.saucedemo.com/"
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
            # ("performance_glitch_user", "secret_sauce"),
            # ("problem_user", "secret_sauce"),
            # pytest.param(
            #     "locked_out_user",
            #     "secret_sauce",
            #     marks=pytest.mark.xfail(raises=AssertionError),
            # ),
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
        # Создает экземпляр главной страницы - Main Page
        # Creates the Product Page instance
        page = ProductsPage(d, link)
        # open product page
        page.open_page()
        # Проверяет, что текущая страница является страницей каталога товаров
        # Checks that the current page is Products Page
        page.should_be_products_page()

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
    #
    # Тест проверяет, что пользователь может перейти со страницы каталога товаров
    # на страницу корзины
    # The test checks that the user can get to the Product Page
    # from Authorization Page
    def test_user_can_go_to_cart_page_from_product_page(self, d, username, password):
        self.test_user_can_go_to_products_page(d, username, password)
        link = "https://www.saucedemo.com/cart.html"
        # Создает экземпляр страницы корзины - Cart Page
        # Creates the Cart Page instance
        page = CartPage(d, link)
        # Open cart page
        page.open_page()
        # Проверяет, что текущая страница является страницей корзины
        # Checks the current page is Cart Page
        page.should_be_cart_page()

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
    # Тест выполнения предусловий:
    # 1. проверяет, что корзина пуста
    # 2. если нет, то удаляет из корзины все товары
    def test_preconditions(self, d, username, password):
        # autorization
        self.test_register_user(d, username, password)
        # go to cart page
        link = "https://www.saucedemo.com/cart.html"
        # Creates the Cart Page instance
        page = CartPage(d, link)
        # Open cart page
        page.open_page()
        # Clear cart
        page.clear_cart()
        page.click_logout_from_top_left_menu()

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
        selected_item = "Test.allTheThings() T-Shirt (Red)"
        # Part 1
        # User's authorization
        self.test_register_user(d, username, password)
        link = "https://www.saucedemo.com/inventory.html"
        # Creates the Product Page instance
        page = ProductsPage(d, link)
        # open products page
        page.open_page()
        # Checks that the current page is Products Page
        page.should_be_products_page()
        # Add Test.allTheThings() T-Shirt (Red) into cart
        page.add_item_on_products_page(selected_item)
        # go to the cart page
        link = "https://www.saucedemo.com/cart.html"
        page = CartPage(d, link)
        page.open_page()
        page.should_be_cart_page()
        # Check that the selected item is in the cart
        page.check_this_item_is_presents_in_the_cart(selected_item)
        # Logout
        page.click_logout_from_top_left_menu()

        # Part 2
        # User's authorization
        self.test_register_user(d, username, password)
        # go to the cart page
        link = "https://www.saucedemo.com/cart.html"
        page = CartPage(d, link)
        page.open_page()
        page.should_be_cart_page()
        # Check that the selected item is in the cart
        page.check_this_item_is_presents_in_the_cart(selected_item)

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
    # Тест выполнения предусловий:
    # 1. проверяет, что корзина пуста
    # 2. если нет, то удаляет из корзины все товары
    def test_postconditions(self, d, username, password):
        self.test_preconditions(d, username, password)
