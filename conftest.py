import json

from selenium import webdriver
import pytest
from selenium.webdriver.edge.options import Options as EdgeOptions
from data.urls import MICE_PAGE_URL, MOUSE_SEARCH_PAGE_URL
from pages.mice_page import MicePage
from pages.mice_search_page import MiceSearchPage
from utils import save_data_to_file
from browsermobproxy import Server
from msedge.selenium_tools import Edge


@pytest.fixture(scope="session", autouse=True)
def save_d():
    save_data_to_file()


@pytest.fixture
def options():
    # options = Options()
    # options = FirefoxOptions()
    options = EdgeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    return options


@pytest.fixture
def driver(options):
    # driver = webdriver.Chrome(options=options)
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def mice_page_fixture(driver):
    mice_page = MicePage(driver, MICE_PAGE_URL)
    yield mice_page


@pytest.fixture(scope='function')
def mouse_search_page_fixture(driver):
    mouse_search_page = MiceSearchPage(driver, MOUSE_SEARCH_PAGE_URL)
    yield mouse_search_page


@pytest.fixture(scope="session")
def expected_dta():
    with open("data/data.json", "r") as f:
        expected_data = json.load(f)
    yield expected_data
