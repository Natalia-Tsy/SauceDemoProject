import pytest
# from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"


class TestSample:
    #
    # Тест проверяет, что пользователь может выполнить авторизацию пользователя
    # The test checks that the User can perform user's authorization
    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            # ("locked_out_user", "secret_sauce"),
            # ("performance_glitch_user", "secret_sauce"),
            # ("problem_user", "secret_sauce"),
        ],
    )
    def test_register_user(self, d, username, password):
        # Creates the Authorization Page instance
        page = LoginPage(d, link)
        # Opens the Authorization Page
        page.open_page()
        # Checks that the current page is Authorization Page
        page.should_be_login_page()
        # User's authorization
        page.register_user(username, password)

    #
    # The test checks that the user can get to the Product Page
    # from Authorization Page
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
    def test_user_can_go_to_products_page(self, d, username, password):
        # User's authorization
        self.test_register_user(d, username, password)
        # if Users == ("locked_out_user", "secret_sauce"):
        #     pytest.xfail()
        link = "https://www.saucedemo.com/inventory.html"
        # Создает экземпляр главной страницы - Main Page
        # Creates the Product Page instance
        page = ProductsPage(d, link)
        # Проверяет, что текущая страница является страницей каталога товаров
        # Checks that the current page is Products Page
        page.should_be_products_page()

    #
    # Тест проверяет, что пользователь находясь на странице каталога  может
    # добавлять/удалять товары в/из корзин
    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
        ],
    )
    def test_user_can_add_items_to_cart_from_product_page(self, d, username, password):
        # User's authorization
        self.test_register_user(d, username, password)
        # if Users == ("locked_out_user", "secret_sauce"):
        #     pytest.xfail()
        link = "https://www.saucedemo.com/inventory.html"
        # Creates the Product Page instance
        page = ProductsPage(d, link)
        # Checks that the current page is Products Page
        page.should_be_products_page()
        # Products that were selected by name are added to/removed from the cart
        # and the list of these products is returned
        page.add_item_on_products_page("Test.allTheThings() T-Shirt (Red)")
        # # Переходит на страницу корзины
        # # Gets to the Cart Page
        # ????? page.go_to_basket_page()

    # #
    # # Тест проверяет, что пользователь может перейти со страницы каталога товаров
    # # на страницу корзины
    # # The test checks that the user can get to the Product Page
    # # from Authorization Page
    # @pytest.mark.parametrize(
    #     "username, password",
    #     [
    #         ("standard_user", "secret_sauce"),
    #         # ("performance_glitch_user", "secret_sauce"),
    #         # ("problem_user", "secret_sauce"),
    #         # pytest.param(
    #         #     "locked_out_user",
    #         #     "secret_sauce",
    #         #     marks=pytest.mark.xfail(raises=AssertionError),
    #         # ),
    #     ],
    # )
    # def test_user_can_go_to_cart_page(self, d, username, password):
    #     self.test_user_can_go_to_products_page(d, username, password)
    #     link = "https://www.saucedemo.com/cart.html"
    #     # Создает экземпляр страницы корзины - Cart Page
    #     # Creates the Cart Page instance
    #     page = CartPage(d, link)
    #     # Проверяет, что текущая страница является страницей корзины
    #     # Checks the current page is Cart Page
    #     page.should_be_cart_page()
