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

#QTY of the first product
    def qty_first_product_shipping_page(self):
       self.list = self.driver.find_elements(By.CSS_SELECTOR,"html>body>div>section>article>div>table>tbody>tr>td>label")
       qty= self.list[4].text
       qty = int(qty)
       return qty

# QTY of the second product
    def qty_second_product_shipping_page(self):
        self.list = self.driver.find_elements(By.CSS_SELECTOR, "html>body>div>section>article>div>table>tbody>tr>td>label")
        qty = self.list[10].text
        qty = int(qty)
        return qty



