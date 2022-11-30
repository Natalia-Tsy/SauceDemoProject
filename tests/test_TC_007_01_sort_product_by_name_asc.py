import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

#sort product
class Tests:
    # TC 007.00.01 Sorting products by name asc
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
    def test_TC_007_01_sort_products_by_name_asc(self, d, username, password):
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)
        page.open_page()
        page.register_user(username, password)
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)
        page.should_be_products_page()
        # sorting from A to Z
        page.sorting_products_by_name_asc()
