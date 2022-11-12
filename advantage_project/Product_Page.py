from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from re import sub


class Product_Page:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def color_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[id='rabbit']")

    # choose a number of color . the left color is "1"
    def choose_color_click(self, num_of_color):
        num_of_color -= 1
        self.color_product()[num_of_color].click()

    # return the name of color according to the choice of color . the left color is "1"
    def name_color(self, num_of_color_chossen: int):
        num_of_color_chossen -= 1
        return self.color_product()[num_of_color_chossen].get_attribute("title")

    def quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name = 'quantity']")

    # input QTY with num type str
    def input_quantity(self, num: str):
        self.quantity().send_keys([Keys.BACKSPACE] * 1000)
        self.quantity().send_keys(num)

    def plus_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, " [class ='plus']")

    def minus_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, " [class ='minus disableBtn']")

    def add_cart(self):
        return self.driver.find_element(By.NAME, "save_to_cart")

    # click on add to cart
    def click_add_cart(self):
        self.add_cart().click()

    # return the name of product
    def name_product(self):
        self.name = self.driver.find_element(By.CSS_SELECTOR, " [class='roboto-regular screen768 ng-binding']")
        return self.name.text

    # return the price of product without $ , type float
    def price_product_float(self):
        self.price = self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-thin screen768 ng-binding']")
        self.price = self.price.text
        self.price = self.price[1:]
        self.price1 = self.price = float(sub(r'[^\d.]', '', self.price))
        return self.price1
