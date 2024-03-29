import pytest
import os
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from demoqa_tests.utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--browser_version', action='store', default="99.0")


@pytest.fixture(scope='function', autouse=True)
def open_browser(request):
    browser_name = request.config.getoption('browser_name')
    browser_version = request.config.getoption('browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": f"{browser_name}",
        "browserVersion": f"{browser_version}",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    if browser_name == 'chrome':
        attach.add_logs(browser)
    browser.quit()