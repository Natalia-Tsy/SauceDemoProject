import pytest
import conf
from selenium import webdriver as WB
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def d(browser):
    if browser == "chrome":
        o = WB.ChromeOptions()
        o.headless = conf.BROWSER_HEADLESS
        driver = WB.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=o,
        )
    elif browser == "firefox":
        o = WB.FirefoxOptions()
        o.headless = conf.BROWSER_HEADLESS
        driver = WB.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="define browser: chrome or firefox, --browser=chrome",
    )


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def g(d):
    print("\n*** start fixture = setup ***\n")
    d.get(conf.URL)
    yield d
    d.quit()
    print("\n*** end fixture = teardown ***\n")


# Убрать комментарии после оформления html report
# def pytest_html_report_title(report):
#     report.title = "REPORT"
