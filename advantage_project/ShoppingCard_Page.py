from selenium import webdriver
from selenium.webdriver.common.by import By

class ShoppingCard_Page:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def shopping_card_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']").text

