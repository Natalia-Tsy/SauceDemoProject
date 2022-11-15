from selenium.webdriver.common.by import By


class ProductsPageLocators:
    TITLE = (By.CLASS_NAME, "title")
    INVENT_LIST = (By.CLASS_NAME, "inventory_list")
    SHOP_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    INVENT_ITEM = (By.CLASS_NAME, "inventory_item_description")


class LoginPageLocators:
    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    LOGIN_CREDENTIALS = (By.ID, "login_credentials")
    LOGIN_PASSWORD = (By.CLASS_NAME, "login_password")
    ERROR_BTN = (By.CLASS_NAME, "error-message-container.error")
