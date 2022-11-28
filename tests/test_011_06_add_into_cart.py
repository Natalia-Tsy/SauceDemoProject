import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


print("\nstart browser...")
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1600,1080")
options.headless = True
browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
# yield browser
print("\nquit browser...")
# browser.quit()
browser.get("https://www.saucedemo.com/")


class Tests:
    def test_add_items_into_cart(self):
        browser.find_element(By.ID, "user-name").send_keys("standard_user")
        browser.find_element(By.XPATH, "//input[@id='password']").send_keys(
            "secret_sauce"
        )
        browser.find_element(By.XPATH, "//input[@name='login-button']").click()
        browser.get("https://www.saucedemo.com/inventory.html")
        browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()
        browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light"
        ).click()
        browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        browser.find_element(By.CSS_SELECTOR, "#continue-shopping").click()
        browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket"
        ).click()
        browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        # browser.find_element(By.CSS_SELECTOR, '#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)').click()

        quantity = browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        if quantity == 5:
            assert "5 item in the cart", "Something went wrong"
