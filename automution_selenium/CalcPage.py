from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def num1(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-model='first']")

    def num2(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-model='second']")

    def op(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")

    def num1_value(self):
        return self.num1().get_attribute("value")

    def num2_value(self):
        return self.num2().get_attribute("value")

    def type_num1(self, num1: str):
        self.num1().send_keys(num1)

    def type_num2(self, num2 : str):
        self.num2().send_keys(num2)

    def choose_op(self, operator:str):
        op_dropdown = Select(self.op())
        op_dropdown.select_by_visible_text(operator)

    def go_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,"#gobutton")

    def go_click(self):
        self.go_button().click()

    def result(self):
        return self.driver.find_element(By.CSS_SELECTOR,"h2.ng-binding")

    def final_result_text(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td.ng-binding")))
        return self.result().text

