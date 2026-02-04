import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Remote
from utils import attach
from dotenv import load_dotenv
import os


load_dotenv()

selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")

def pytest_addoption(parser):
    parser.addoption(
        '--browserVersion',
        help='Браузер в котором будут запущены тесты',
        default='127.0'
    )

@pytest.fixture(scope='function', autouse=True)
def browser_setup(request):
    browser_version = request.config.getoption('--browserVersion')
    browser.config.base_url = 'https://demoqa.com'
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': browser_version,
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True,
            'screenResolution': '1920x1080x24'
        }
    }

    options.capabilities.update(selenoid_capabilities)

    remote_driver = Remote(
        command_executor=selenoid_url,
        options=options
    )

    browser.config.driver = remote_driver

    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()