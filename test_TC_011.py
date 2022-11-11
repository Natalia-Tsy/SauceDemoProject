import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


print("\nstart browser...")
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1600,1080")
options.headless = True
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
# yield browser
print("\nquit browser...")
# browser.quit()

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.saucedemo.com/")


def test_title():
    title_from_site = driver.title
    assert title_from_site == "Swag Labs"


def test_login_form():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@name='login-button']").click()
    time.sleep(2)

    assert (
        driver.current_url == "https://www.saucedemo.com/inventory.html"
    ), "We reached another site!"
