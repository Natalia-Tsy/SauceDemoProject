import pytest
import conf
import os
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        feature_request = item.funcargs["request"]
        driver = feature_request.getfixturevalue("d")
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_dir = os.path.dirname(item.config.option.htmlpath)
            nodeid_ = report.nodeid
            file_name = (
                report.nodeid[len(os.path.dirname(item.nodeid)) :].replace("::", "_")[
                    1:
                ]
                + ".png"
            )
            destination_file = os.path.join(report_dir, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                # chrome_browser.save_screenshot('C:/Users/user/Desktop/demo.png')
                html = (
                    '<div><img src="%s" alt="screenshot" style="width:300px;height:200px" onclick="window.open('
                    'this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "REPORT"
