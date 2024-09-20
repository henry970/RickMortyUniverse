import pytest
from selenium import webdriver

from ActionPage.actionpage import RickMortyUniversePages


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def launch(driver_setup):
    driver = driver_setup
    landing_page = RickMortyUniversePages(driver)
    landing_page.open_web_page("https://d28dp6fycxce58.cloudfront.net/")
    return landing_page


def test_login_page_on_rick_morty_universe_pages_website(launch):
    launch.enter_name("morty")
    launch.click_location_drop_down_button()
    launch.select_location()
