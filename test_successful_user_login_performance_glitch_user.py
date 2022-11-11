import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def init_browser():
    """Функция создания драйвера Хром"""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return browser


def test_login_user_performance_glitch_user(browser:webdriver.Chrome):
    """Тест проверки успешной авторизации пользователя performance_glitch_user"""
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys('performance_glitch_user')
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR,"input[placeholder='Password']").send_keys('secret_sauce')
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR,"#login-button").click()
    time.sleep(2)
    login_url = browser.current_url
    assert "https://www.saucedemo.com/inventory.html" == login_url, "The current page does not correspond to the page the user should be on after successful registration"


if __name__ == '__main__':
    browser = init_browser()
    test_login_user_performance_glitch_user(browser)
