from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Product_Page:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def color_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[id='rabbit']")

    def choose_color(self, num_of_color):
        num_of_color = num_of_color - 1
        self.color_product()[num_of_color].click()

    def quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name = 'quantity']")

    def input_quantity(self, num:str):
        self.quantity().send_keys([Keys.BACKSPACE] * 1000)
        self.quantity().send_keys(num)

    def plus_button(self):
        return self.driver.find_element(By.CSS_SELECTOR," [class ='plus']")

    def minus_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, " [class ='minus disableBtn']")

    def add_cart(self):
        return self.driver.find_element(By.NAME, "save_to_cart")

    def click_add_cart(self):
        self.add_cart().click()

    def name_product(self):
        self.driver.find_element(By.CSS_SELECTOR, " [class='roboto-regular screen768 ng-binding']")
        return self.driver.text()

    #def color_name(self):

    def price_product_float(self):
        self.price = self.driver.find_elements(By.CSS_SELECTOR, "[class='roboto-thin screen768 ng-binding']")
        self.price = self.price[0].text
        self.price = self.price[1:]
        self.price = float(self.price)
        return self.price









