import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.saucedemo.com/")


def test_title():
    title_from_site = driver.title
    assert title_from_site == "Swag Labs"


def test_login_form():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@name='login-button']").click()
    time.sleep(3)

    assert (
        driver.current_url == "https://www.saucedemo.com/inventory.html"
    ), "We reached another site!"
