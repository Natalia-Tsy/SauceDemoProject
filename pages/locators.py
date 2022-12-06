from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    LOGIN_CREDENTIALS = (By.ID, "login_credentials")
    LOGIN_PASSWORD = (By.CLASS_NAME, "login_password")
    ERROR_BTN = (By.CLASS_NAME, "error-message-container.error")


class ProductsPageLocators:
    TITLE = (By.CLASS_NAME, "title")
    INVENT_LIST = (By.CLASS_NAME, "inventory_list")
    SHOP_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    INVENT_ITEM = (By.CLASS_NAME, "inventory_item_description")
    # for test TC_007_01
    PRODUCT_IMG = (By.CSS_SELECTOR, "#item_0_img_link>img")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#item_0_title_link>div")
    PRODUCT_PRICE = (
        By.XPATH,
        "//*[@id = 'item_0_title_link']/ancestor::*[@class = 'inventory_item_description']//*[@class = 'inventory_item_price']",
    )
    PRODUCT_IMG_FOR_CLICK = (By.CSS_SELECTOR, "#item_0_img_link")
    # for sort product
    SORTING_BY_NAME_AZ = (By.CSS_SELECTOR, '.product_sort_container option[value="az"]')

    # Rustam
    INVENTORY_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    INVENTORY_ITEM_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
    INVENTORY_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    INVENTORY_ITEM_LINK = (By.CSS_SELECTOR, ".inventory_item_img .inventory_item_img")

    SAUCE_LABS_BACKPACK_ADD_TO_CART = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-backpack",
    )
    SAUCE_LABS_BACKPACK_REMOVE_FROM_CART = (
        By.CSS_SELECTOR,
        "#remove-sauce-labs-backpack",
    )
    SORT_DROPDOWN = (By.CLASS_NAME, "select_container")
    PRICE_LOW_TO_HIGH = (By.CSS_SELECTOR, ".product_sort_container [value='lohi']")


class CartPageLocators:
    CHECKOUT_BTN = (By.ID, "checkout")
    TITLE = (By.CLASS_NAME, "title")
    QUANTITY = (By.CLASS_NAME, "shopping_cart_badge")
    LIST_OF_PRODUCTS = (By.CSS_SELECTOR, ".cart_list > .cart_item")
    LIST_OF_NAME_PRODUCTS = (
        By.CSS_SELECTOR,
        ".cart_list > .cart_item div.inventory_item_name",
    )
    LIST_OF_REMOVE_BUTTON_ELEMENTS = (By.CSS_SELECTOR, ".cart_list > .cart_item button")
    PRODUCT_NAME_OF_ITEM = (By.CSS_SELECTOR, "div.inventory_item_name")
    QTY_OF_ITEM = (By.CSS_SELECTOR, "div.cart_quantity")
    PRICE_OF_ITEM = (By.CSS_SELECTOR, "div.inventory_item_price")

class Chckout1PageLocators:
    CONTINUE_BTN = (By.ID, "continue")
    TITLE = (By.CLASS_NAME, "title")
    INPUT_FIRSTNAME = (By.ID, "first-name")
    INPUT_LASTNAME = (By.ID, "last-name")
    INPUT_CODE = (By.ID, "postal-code")


class Chckout2PageLocators:
    FINISH_BTN = (By.ID, "finish")
    TITLE = (By.CLASS_NAME, "title")


class CheckoutCmpltPageLocators:
    BACKHOME_BTN = (By.ID, "back-to-products")
    TITLE = (By.CLASS_NAME, "title")
    COMPLETE_MSG = (By.CLASS_NAME, "complete - header")
    SHOP_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")


class PageLocators:
    ROBOT_IMG = (By.CSS_SELECTOR, ".footer_robot")
    PRIVACY = (By.XPATH, "//*[@class = 'footer_copy']/text()[3]")


class ProductPageLocators:
    PRODUCT_PRICE_DETAILS = (By.CSS_SELECTOR, ".inventory_details_price")
    PRODUCT_IMG_DETAILS = (By.CSS_SELECTOR, ".inventory_details_img")
    PRODUCT_NAME_DETAILS = (By.CSS_SELECTOR, ".inventory_details_name")


class SideBarLocator:
    HAMBURGER = (By.ID, "react-burger-menu-btn")
    ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    LOGOUT = (By.ID, "logout_sidebar_link")
