import time
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


# TC 003.00 Login page with another username
class TestSample:
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
    def test_TC_003_user_сan_autorize(self, d, username, password):
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)
        page.open_page()
        page.register_user(username, password)
        time.sleep(2)
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)
        page.should_be_products_page()
