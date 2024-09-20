import time
from os import times

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.locatorPage import RickMortyUniverseLocatorsPage


class RickMortyUniversePages:
    def __init__(self, driver):
        self.driver = driver

    def open_web_page(self, url):
        self.driver.get(url)

    def enter_name(self, name):
        enter_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RickMortyUniverseLocatorsPage.ENTER_NAME))
        enter_name.send_keys(name)
        time.sleep(5)

    def click_location_drop_down_button(self):
        click_location_drop_down_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RickMortyUniverseLocatorsPage.CLICK_DROP_DOWN))
        click_location_drop_down_button.click()
        time.sleep(5)

    def select_location(self):
        select_location = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(RickMortyUniverseLocatorsPage.SELECT_LOCATION))
        select_location.click()
