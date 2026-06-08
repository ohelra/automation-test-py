import os
import json
import platform
import sys
import pytest_html
import undetected_chromedriver as uc
from selenium import webdriver
import pytest
import base64
from undetected_chromedriver import ChromeOptions
from utilities.custom_logger import LogMaker
from utilities.read_properties import ReadConfig

# ================== GLOBAL LOG ==================
logger = LogMaker.log_gen()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",help="Browser: chrome, firefox or edge")

@pytest.fixture(scope="class")                                         # Fixture (scope="class") only runs once for the entire test class and shares the same driver for all tests in that class.
def setup(request):                                                    # The object to know which test is calling this fixture

    browser = request.config.getoption("--browser") or "chrome"
    if browser == "chrome":
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--headless=new")
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--force-device-scale-factor=1")
        #
        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        # chrome_options.add_argument(f"user-agent={user_agent}")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)
        # driver.set_window_size(1920, 1080)
        # driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
        #     "width": 1920,
        #     "height": 1080,
        #     "deviceScaleFactor": 1,
        #     "mobile": False,
        #     "screenOrientation": {"type": "landscapePrimary", "angle": 0}
        # })

    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser!")

    driver.maximize_window()
    driver.implicitly_wait(10)

    if request.cls is not None:                                       # Manually assign fixture to self
        request.cls.driver = driver                                   # Support_Pages every function in the class access self.driver.

    yield driver
    driver.quit()


# ================== PYTEST HTML REPORT ==================
@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "RSPRO Website Automation Report"

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"<p><b>Project:</b> RSPRO Website</p>"])
    prefix.extend([f"<p><b>Tester:</b> Huynh Quoc Thang</p>"])


# ================== EVIDENCES ==================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        if rep.failed:
            driver = item.funcargs.get("setup")
            if driver:
                screenshot_dir = os.path.join(os.getcwd(), "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)

                screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
                driver.save_screenshot(screenshot_path)

                with open(screenshot_path, "rb") as f:
                    image_base64 = base64.b64encode(f.read()).decode("utf-8")
                extra_html = f'<div><img src="data:image/png;base64,{image_base64}" width="400"/></div>'
                if hasattr(rep, "extra"):
                    rep.extra.append(pytest_html.extras.html(extra_html))
                else:
                    rep.extra = [pytest_html.extras.html(extra_html)]

            logger.failed(f"{item.name} - Failed")
        elif rep.passed:
            logger.passed(f"{item.name} - Pass")



# # ================== AUTO GENERATE REPORT ==================
# def pytest_sessionfinish(session, exitstatus):
#     os.system("pytest --html=report.html --self-contained-html")
