from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from CalcPage import CalcPage


class TestCalcPage(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")

        # Open browser (create a driver object)
        self.driver = webdriver.Chrome(service=service_chrome)

        # Go to the required URL
        self.driver.get("https://juliemr.github.io/protractor-demo/")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # create object
        self.calc_page = CalcPage(self.driver)

    def test_default_value(self):
        self.assertEqual(self.calc_page.num1_value(), "")
        self.assertEqual(self.calc_page.num2_value(), "")

    def test_result(self):
        self.calc_page.type_num1('12')
        self.calc_page.type_num2('3')
        self.calc_page.choose_op('*')

        self.calc_page.go_click()
        self.assertEqual(self.calc_page.final_result_text(), '36')

