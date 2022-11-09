from selenium import webdriver
from selenium.webdriver.common.by import By

class ShoppingCard_Page:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def shopping_card_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']").text

    def edit_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"[class='edit ng-scope']")

    def click_edit_product(self, num):
        num -= 1
        return self.driver.execute_script("arguments[0].click();", self.edit_product()[num])


    def details_product_shopping_page(self):
       list = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td>label")
       return list.text

