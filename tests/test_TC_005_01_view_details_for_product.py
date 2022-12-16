# -*- coding: utf-8 -*-
# @Time    : 2022/11/15 16:55
# @Author  : Mariya Abayev

import pytest
import allure
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.products_page import ProductsPage
from src.src import LoginPageSrc, ProductsPageSrc, ProductPageSrc


class Tests:
    @allure.feature("US_005 | View product page")
    @allure.story("TC_005.01 | View details for product from products page")
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
    def test_TC_005_01_view_details_for_product(self, d, username, password):
        page = LoginPage(d, LoginPageSrc.URL)
        page.open_page()
        page.register_user(username, password)
        page = ProductsPage(d, ProductsPageSrc.URL)
        page.should_be_products_page()
        item = page.select_product()
        page.go_to_product_page()
        page = ProductPage(d, ProductPageSrc.LINK)
        page.should_be_product_page()
        page.check_product_img(item)
        page.check_product_name(item)
        page.check_product_price(item)
