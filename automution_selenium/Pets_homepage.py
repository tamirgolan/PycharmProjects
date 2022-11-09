from selenium import webdriver
from selenium.webdriver.common.by import By


class Pets_homepage:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def choose_category(self,num):
       return self.driver.find_elements(By.CSS_SELECTOR, "#SidebarContent>a>img")

    def click_category(self, num):
        self.choose_category(num).click()

