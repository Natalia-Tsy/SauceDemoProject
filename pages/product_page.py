from .base_page import BasePage
from src.src import ProductPageSrc
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """This class is used to test the functionality of the product page of the website.

    Args:
        BasePage: Contains common methods that are used by all page classes
    """

    def should_be_product_page(self):
        """Check that the current page is the product page."""
        self.should_be_link(ProductPageSrc.LINK)

    def check_product_img(self, mydict):
        """Check img"""
        select_img = self.get_src(0, *ProductPageLocators.PRODUCT_IMG_DETAILS)
        assert (
            select_img == mydict["img"]
        ), f"The the source URL of the image {select_img} on the product page does not match the expected image {mydict['img']}"

    def check_product_name(self, mydict):
        """Check name"""
        select_name = self.get_text(0, *ProductPageLocators.PRODUCT_NAME_DETAILS)
        assert (
            select_name == mydict["name"]
        ), f"The name {select_name} on the product page does not match the expected name {mydict['name']}"

    def check_product_price(self, mydict):
        """Check price"""
        select_price = self.get_text(0, *ProductPageLocators.PRODUCT_PRICE_DETAILS)
        assert (
            select_price == mydict["price"]
        ), f"The price {select_price} on the product page does not match the expected price {mydict['price']}"
