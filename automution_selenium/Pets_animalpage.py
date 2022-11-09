from selenium import webdriver
from selenium.webdriver.common.by import By


class Pets_animalpage:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def choose_product(self, num):
        return self.driver.find_elements(By.CSS_SELECTOR, "td>a")

    def click_product(self, num):
        return self.choose_product(num).click()


