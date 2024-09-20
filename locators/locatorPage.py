from selenium.webdriver.common.by import By


class RickMortyUniverseLocatorsPage:
    ENTER_NAME = (By.XPATH, '/html/body/div/div/div[1]/div/input')
    CLICK_DROP_DOWN = (By.XPATH, '/html/body/div/div/div[1]/div/div/select')
    SELECT_LOCATION = (By.XPATH, '/html/body/div/div/div[1]/div/div/select/option[4]')
