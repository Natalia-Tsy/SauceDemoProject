import pytest
import conf
from selenium import webdriver as WB
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def d(browser):
    if browser == "chrome":
        o = WB.ChromeOptions()
        o.headless = conf.BROWSER_HEADLESS
        driver = WB.Chrome(
            service=ChromiumService(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=o,
        )
    elif browser == "firefox":
        o = WB.FirefoxOptions()
        o.headless = conf.BROWSER_HEADLESS
        driver = WB.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
    elif browser == "chromeport":
        chromedriverpath = "D:\\Program  Files\\GoogleChromePortable_last\\chromedriver.exe"  # Для portable версии Chrome
        chromePath = "D:\\Program  Files\\GoogleChromePortable_last\\App\\Chrome-bin\\chrome.exe"  # Для portable версии Chrome
        o = Options()  # Для portable версии Chrome
        o.binary_location = chromePath
        o.headless = conf.BROWSER_HEADLESS
        driver = WB.Chrome(executable_path=chromedriverpath, options=o)
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="firefox",
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


# def pytest_html_report_title(report):
#     report.title = "REPORT"
