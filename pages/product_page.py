from .base_page import BasePage
from .src import ProductPageSrc
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Checks that the current page is Product page
    def should_be_product_page(self):
        # Checks that the current page meets the requirements
        self.should_be_link(ProductPageSrc.LINK)

    def check_product_img(self, mydict):
        """Check img"""
        select_img = self.get_src(0, *ProductPageLocators.PRODUCT_IMG_DETAILS)
        assert select_img == mydict["img"], "We found another name of product"

    def check_product_name(self, mydict):
        """Check name"""
        select_name = self.get_text(0, *ProductPageLocators.PRODUCT_NAME_DETAILS)
        assert select_name == mydict["name"], "We found another name of product"

    def check_product_price(self, mydict):
        """Check price"""
        select_price = self.get_text(0, *ProductPageLocators.PRODUCT_PRICE_DETAILS)
        assert select_price == mydict["price"], "We found another price"
