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
    PRODUCT_IMG = (By.CSS_SELECTOR, "#item_0_img_link>img")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#item_0_title_link>div")
    PRODUCT_NAME_DETAILS = (By.CSS_SELECTOR, ".inventory_details_name")
    BACK_TO_PRODUCTS = (By.CSS_SELECTOR, "#back-to-products")
    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "#inventory_container > div > div:nth-child(2) > div.inventory_item_description > div.pricebar > div",
    )
    PRODUCT_PRICE_DETAILS = (By.CSS_SELECTOR, ".inventory_details_price")
    PRODUCT_IMG_DETAILS = (By.CSS_SELECTOR, ".inventory_details_img")
    PRODUCT_IMG_FOR_CLICK = (By.CSS_SELECTOR, "#item_0_img_link")
    SORTING_BY_NAME_AZ = (By.CSS_SELECTOR, 'option[value="az"]')
    ALL_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    SORTING_BY_PRICE_ASC = (By.CSS_SELECTOR, 'option[value="lohi"]')
    All_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")


class CartPageLocators:
    CHECKOUT_BTN = (By.ID, "checkout")
    TITLE = (By.CLASS_NAME, "title")
    QUANTITY = (By.CLASS_NAME, "shopping_cart_badge")


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
    HAMBURGER = (By.ID, "react-burger-menu-btn")
    ALL_ITEMS = (By.ID, "inventory_sidebar_link")
