import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.products_page import ProductsPage

# view_details_for_product


class Tests:
    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce"),
            pytest.param(
                "locked_out_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
            pytest.param(
                "problem_user",
                "secret_sauce",
                marks=pytest.mark.xfail(raises=AssertionError),
            ),
        ],
    )
    # view details
    def test_TC_005_01_view_details_for_product(self, d, username, password):
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)
        page.open_page()
        page.register_user(username, password)
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)
        page.should_be_products_page()
        item = page.select_product()
        page.go_to_product_page()
        page = ProductPage(d, link)
        page.should_be_product_page()
        page.check_product_img(item)
        page.check_product_name(item)
        page.check_product_price(item)
