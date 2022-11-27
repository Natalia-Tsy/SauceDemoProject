import pytest
from selenium.common import NoSuchElementException

from pages.basket_page import BasketPage

link = "https://www.saucedemo.com/"


class TestBasketPage:

    @pytest.mark.parametrize(
        "username, password, products",
        [
            ("standard_user", "secret_sauce",
             ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
              "Test.allTheThings() T-Shirt (Red)"]),
            ("performance_glitch_user", "secret_sauce",
             ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
              "Test.allTheThings() T-Shirt (Red)"]),

            pytest.param(
                "locked_out_user",
                "secret_sauce",
                ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
                 "Test.allTheThings() T-Shirt (Red)"],
                marks=pytest.mark.xfail(raises=(AssertionError, NoSuchElementException)),

            ),
            pytest.param(
                "problem_user",
                "secret_sauce",
                ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
                 "Test.allTheThings() T-Shirt (Red)"],
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    def test_add_products_in_basket_from_main_page(self, d, username, password, products):
        """Тест проверки соответствия количества товаров на странице корзины и на иконке корзины на главной странице """
        page = BasketPage(d, link)
        # Открывает страницу авторизации
        page.open_page()
        # Регистрация пользователя
        page.register_user(username, password)
        # Добавление товаров с главной страницы
        page.put_or_del_products_in_packet(products)
        # Удаление товаров с главной страницы
        page.put_or_del_products_in_packet(products)
        # Получение количества товаров с иконки корзины
        num_products_after_add_in_basket = page.view_and_remember_the_number_product_on_icon_basket()
        # Получение данных со страницы корзины и сравнение количества товаров отображаемых в корзине и на иконке корзины
        page.get_data_about_products_in_basket(num_products_after_add_in_basket)
