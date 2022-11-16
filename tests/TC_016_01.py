from ..pages.cart_page import CartPage
from ..pages.products_page import ProductsPage
from ..pages.login_page import LoginPage
from ..pages.checkout_1_page import CheckoutPage_1
from ..pages.checkout_2_page import CheckoutPage_2
from ..pages.checkout_cmplt_page import CheckouCmpltPage
import pytest

link = "https://www.saucedemo.com/"


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "performance_glitch_user",
        "problem_user",
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
        "performance_glitch_user",
        "problem_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
# Тест проверяет, что пользователь может перейти со страницы авторизации
# на страницу каталога товаров
def test_user_can_go_to_products_page(browser, username, password):
    # Авторизация пользователя
    test_register_user(browser, username, password)
    # if Users == ("locked_out_user", "secret_sauce"):
    #     pytest.xfail()
    link = "https://www.saucedemo.com/inventory.html"
    # Создает экземпляр главной страницы - Main Page
    page = ProductsPage(browser, link)
    # Проверяет, что текущая страница является страницей каталогом товаров
    page.should_be_products_page()
    # Добавляются в корзину/Удаляются из корзины выбранные по имени товары
    # и возвращает список данных товаров
    page.add_item_on_products_page("Sauce Labs Onesie", "Sauce Labs Backpack")
    # Переходит на страницу корзины
    page.go_to_basket_page()


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "performance_glitch_user",
        "problem_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
# Тест проверяет, что пользователь может перейти со страницы авторизации
# на страницу каталога товаров
def test_user_can_go_to_cart_page(browser, username, password):
    test_user_can_go_to_products_page(browser, username, password)
    link = "https://www.saucedemo.com/cart.html"
    # Создает экземпляр страницы корзины - Cart Page
    page = CartPage(browser, link)
    # Проверяет, что текущая страница является страницей корзины
    page.should_be_cart_page()
    # Переходит на страницу оформления заказа
    page.go_to_checkout_1_page()
    link = "https://www.saucedemo.com/checkout-step-one.html"
    # Создает экземпляр страницы корзины - Cart Page
    page = CheckoutPage_1(browser, link)
    # Проверяет, что текущая страница является страницей корзины
    page.should_be_checkout_1_page()


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "performance_glitch_user",
        "problem_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
# @pytest.mark.parametrize(
#     "firstname",
#     [
#         "John",
#     ],
#     "lastname",
#     [
#         "Smith",
#     ],
#     "code",
#     [
#         "33009",
#     ],
# )
# Тест проверяет, что пользователь может перейти со страницы авторизации
# на страницу каталога товаров
def test_user_can_go_to_checkout_1_page(browser, username, password):
    test_user_can_go_to_cart_page(browser, username, password)
    link = "https://www.saucedemo.com/checkout-step-one.html"
    # Создает экземпляр страницы корзины - Cart Page
    page = CheckoutPage_1(browser, link)
    # Проверяет, что текущая страница является страницей корзины
    page.should_be_checkout_1_page()
    # Заполняются данные, необходимые для получения товара
    page.set_shipping_info("John", "Smith", "33009")
    # Переходит на следующую страницу оформления заказа
    page.go_to_checkout_2_page()
    link = "https://www.saucedemo.com/checkout-step-two.html"
    # Создает экземпляр главной страницы - Main Page
    page = CheckoutPage_2(browser, link)
    # Проверяет, что текущая страница является
    # следующей страницей оформления заказа
    page.should_be_checkout_2_page()


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "performance_glitch_user",
        "problem_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
def test_user_can_go_to_checkout_2_page(browser, username, password):
    test_user_can_go_to_checkout_1_page(browser, username, password)
    link = "https://www.saucedemo.com/checkout-step-two.html"
    # Создает экземпляр главной страницы - Main Page
    page = CheckoutPage_2(browser, link)
    # Проверяет, что текущая страница является
    # следующей страницей оформления заказа
    page.should_be_checkout_2_page()
    # Переходит на страницу завершения оформления заказа
    page.go_to_checkout_complete_page()
    link = "https://www.saucedemo.com/checkout-complete.html"
    # Создает экземпляр главной страницы - Main Page
    page = CheckouCmpltPage(browser, link)
    # Проверяет, что текущая страница является
    # следующей страницей оформления заказа
    page.should_be_checkout_complete_page()


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "locked_out_user",
        "performance_glitch_user",
        "problem_user",
    ],
)
@pytest.mark.parametrize("password", ["secret_sauce"])
def test_user_can_go_to_checkout_complete_page(browser, username, password):
    test_user_can_go_to_checkout_2_page(browser, username, password)
    link = "https://www.saucedemo.com/checkout-complete.html"
    # Создает экземпляр главной страницы - Main Page
    page = CheckouCmpltPage(browser, link)
    # Проверяет, что текущая страница является
    # следующей страницей оформления заказа
    page.should_be_checkout_complete_page()
    # Переходит на страницу каталога товаров
    page.go_to_products_page()
    link = "https://www.saucedemo.com/inventory.html"
    # Создает экземпляр главной страницы - Main Page
    page = ProductsPage(browser, link)
    # Проверяет, что текущая страница является страницей каталогом товаров
    page.should_be_products_page()
    # Проверяет, что иконка корзины на текущей странице не указывает
    # количество товаров в корзине
    page.should_be_empty_shopping_cart_badge()
