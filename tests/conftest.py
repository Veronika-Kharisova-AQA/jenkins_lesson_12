import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv
import os

selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.base_url = 'https://demoqa.com'
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': '127.0',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True,
            'screenResolution': '1920x1080x24'
        }
    }
    options.capabilities.update(selenoid_capabilities)
    browser.config.driver_options = options
    browser.config.driver_remote_url = 'https://user1:1234@selenoid.autotests.cloud/wd/hub'

    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()