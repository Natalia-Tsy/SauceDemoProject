from ..pages.products_page import ProductsPage
from ..pages.login_page import LoginPage
from ..pages.cart_page import CartPage


class Tests:
    def test_return_to_the_catalog(self, d):
        link = "https://www.saucedemo.com/"
        page = LoginPage(d, link)  # Creates the Login page instance
        page.open_page()
        page.register_user("standard_user", "secret_sauce")  # Standard user logs in
        link = "https://www.saucedemo.com/inventory.html"
        page = ProductsPage(d, link)  # Creates the Products page instance
        page.should_be_products_page()
        page.add_item_on_products_page(
            "Sauce Labs Fleece Jacket", "Test.allTheThings() T-Shirt (Red)"
        )
        page.go_to_basket_page()  # gets to the Cart page
        link = "https://www.saucedemo.com/cart.html"
        page = CartPage(d, link)
        page.check_the_quantity()  # checks the cart is not empty
        page.open_hamburger()
        page.click_all_items()
        page = ProductsPage(d, link)  # creates the Products page instance
        page.should_be_products_page()  # Checks we're on the Product page
