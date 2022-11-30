import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


print("\nstart browser...")
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.headless = True
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(ChromeDriverManager().install())

# yield driver

# driver.get("https://www.saucedemo.com/")
time.sleep(1)


# Precondition
def test_login_form():
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@name='login-button']").click()
    time.sleep(1)

    assert (
        driver.current_url == "https://www.saucedemo.com/inventory.html"
    ), "We reached another site!"


# Steps of test_ts015_01 | Save cart data of current user after re-login
def test_tc015_01():
    # Выполнение предусловий
    # test_login_form()   # Выполнение предусловий
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@name='login-button']").click()
    time.sleep(1)

    assert (
        driver.current_url == "https://www.saucedemo.com/inventory.html"
    ), "We reached another site!"

    # 1. Add product "Test.allTheThings() T-Shirt (Red)" to cart on the page https://www.saucedemo.com/inventory.html
    driver.get("https://www.saucedemo.com/inventory.html")

    # css_loc = ".inventory_list .inventory_item_label #item_3_title_link"
    # driver.find_element(By.CSS_SELECTOR, css_loc).click()

    css_loc = "item_3_img_link"
    driver.find_element(By.ID, css_loc).click()
    time.sleep(1)

    url_item = "https://www.saucedemo.com/inventory-item.html?id=3"
    assert driver.current_url == url_item, "Не зашли в карточку нужного товара"

    css_loc = ".inventory_details_desc_container button"
    driver.find_element(By.CSS_SELECTOR, css_loc).click()  # ADD TO CARD
    time.sleep(1)

    # 2. Проверка что добавили товар в корзину
    css_loc = ".shopping_cart_link"
    driver.find_element(By.CSS_SELECTOR, css_loc).click()  # вошли в Корзину
    time.sleep(1)
    assert (
        driver.current_url == "https://www.saucedemo.com/cart.html"
    ), "Не зашли в корзину"

    css_loc = ".cart_list > .cart_item .inventory_item_name"
    item_name = driver.find_element(By.CSS_SELECTOR, css_loc).text
    time.sleep(1)
    assert (
        item_name == "Test.allTheThings() T-Shirt (Red)"
    ), "В корзине нет нужного товара"

    # 3. Сlick the hamburger menu button in the upper left corner of the header. Click "LOGOUT" from the dropdown list
    css_loc = "#react-burger-menu-btn"
    driver.find_element(By.CSS_SELECTOR, css_loc).click()
    time.sleep(1)

    css_loc = "#logout_sidebar_link"
    driver.find_element(By.CSS_SELECTOR, css_loc).click()
    time.sleep(1)
    # проверяем, что вышли из системы на головную страницу
    assert (
        driver.current_url == "https://www.saucedemo.com/"
    ), "Мы не вышли из магазина, на главную страницу авторизации"

    # 4. On the page https://www.saucedemo.com/. Input the username: standard_user and password: secret_sauce
    # and press "Login" button
    test_login_form()

    # 5. Press "Cart" icon on the page "https://www.saucedemo.com/inventory.html"
    css_loc = ".shopping_cart_link"
    driver.find_element(By.CSS_SELECTOR, css_loc).click()  # вошли в Корзину
    time.sleep(1)
    assert (
        driver.current_url == "https://www.saucedemo.com/cart.html"
    ), "Не зашли в корзину"

    css_loc = ".cart_list > .cart_item .inventory_item_name"
    item_name = driver.find_element(By.CSS_SELECTOR, css_loc).text
    assert (
        item_name == "Test.allTheThings() T-Shirt (Red)"
    ), "В корзине нет нужного товара"


print("\nquit browser...")
# browser.quit()