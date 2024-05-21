import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv


@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://allplay.uz'
    # driver_options = webdriver.ChromeOptions()
    # driver_options.page_load_strategy = 'eager'
    # driver_options.add_argument('--no-sandbox')
    # driver_options.add_argument('--enable-automation')
    # driver_options.add_argument("--disable-gpu")
    # driver_options.add_argument("--no-sandbox")
    # driver_options.add_argument('--disable-setuid-sandbox')
    # driver_options.add_argument("--disable-dev-shm-usage")
    # driver_options.add_argument("--incognito")
    # browser.config.driver_options = driver_options
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--enable-automation')
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")
    options.page_load_strategy = 'eager'

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "122.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
