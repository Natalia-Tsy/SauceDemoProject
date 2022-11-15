from ..pages.products_page import ProductsPage
from ..pages.login_page import LoginPage
import pytest

link = "https://www.saucedemo.com/"


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
# Тест проверяет, что пользователь может выполнить авторизацию пользователя
def test_register_user(browser, username, password):
    # Создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # Открывает страницу авторизации
    page.open_page()
    # Проверяет, что текущая страница является страницей авторизации
    page.should_be_login_page()
    # Авторизация пользователя
    page.register_user(username, password)


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
# Тест проверяет, что пользователь может перейти со страницы авторизации
# на страницу каталога товаров
def test_user_can_go_to_products_page(browser, username, password):
    # def test_user_can_go_to_products_page(d, username, password):
    # Создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # Создает экземпляр страницы авторизации
    test_register_user(browser, username, password)
    # if Users == ("locked_out_user", "secret_sauce"):
    #     pytest.xfail()
    # Создает экземпляр главной страницы - Main Page
    page = ProductsPage(browser, link)
    # Проверяет, что текущая страница является страницей каталогом товаров
    page.should_be_products_page()
    # Добавляет выбранные товары в корзину
    page.add_item_on_products_page(
        "Sauce Labs Onesie", "Sauce Labs Fleece Jacket"
    )


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
def test_user_can_not_go_to_products_page(browser, username, password):
    # def test_user_can_go_to_products_page(d, username, password):
    # Создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # Создает экземпляр страницы авторизации
    test_register_user(browser, username, password)
    # Проверяет, что текущая страница является страницей авторизации
    page.should_be_login_page()
    # Проверяет, что на текущей странице отображается сообщение об ошибке
    page.should_be_error_message()
