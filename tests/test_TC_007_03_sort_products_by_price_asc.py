# -*- coding: utf-8 -*-
# @Time    : 2022/11/29 16:55
# @Author  : Mariya Abayev

import pytest
import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from src.src import LoginPageSrc, ProductsPageSrc


class Test:
    @allure.feature("US_007 | Sorting")
    @allure.story("TC_007.03 | Sorting products by price ascending")
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
    def test_TC_007_03_sort_products_by_price_asc(self, d, username, password):
        page = LoginPage(d, LoginPageSrc.URL)
        page.open_page()
        page.register_user(username, password)
        page = ProductsPage(d, ProductsPageSrc.URL)
        page.should_be_products_page()
        page.sorting_products_by_price_asc()
