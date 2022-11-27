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
    NAME_PRODUCT = (By.CSS_SELECTOR, ".inventory_item_name")
    BTN_ADD_OR_DEL_TO_BASKET = (By.CSS_SELECTOR, "button.btn_inventory")


class CartPageLocators:
    CHECKOUT_BTN = (By.ID, "checkout")
    TITLE = (By.CLASS_NAME, "title")


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


class BasketIconMainPageLocators:
    NUMBER_PRODUCT_IN_BASKET = (By.CSS_SELECTOR,".shopping_cart_link > span.shopping_cart_badge")
    ICON_BASKET = (By.CSS_SELECTOR,'#shopping_cart_container')

class BasketPageLocators:
    TITLE = (By.CSS_SELECTOR, ".title")
    BASKET_LIST = (By.CSS_SELECTOR, ".cart_list")
    LIST_PRODUCTS = (By.CSS_SELECTOR,".cart_item")