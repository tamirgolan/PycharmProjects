from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Home_Page import Home_Page
from Category_Page import Category_Page
from Product_Page import Product_Page
from ShoppingCard_Page import ShoppingCard_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TestProduct_Page(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")

        # Open browser (create a driver object)
        self.driver = webdriver.Chrome(service=service_chrome)

        # Go to the required URL
        self.driver.get("https://advantageonlineshopping.com/#/")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # create object
        self.home_page = Home_Page(self.driver)
        self.category_page = Category_Page(self.driver)
        self.product_page = Product_Page(self.driver)
        self.shopping_cart_page = ShoppingCard_Page(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def test_1_correct_final_quantity(self):

       # self.wait.until(EC.visibility_of_element_located((self.home_page.website_logo())))

        #add first product to cart
        self.home_page.click_mice()
        self.category_page.choose_product(1)
        self.product_page.input_quantity('2')
        self.product_page.add_cart()
        #add another product
        self.home_page.click_website_logo()

        #self.wait.until(EC.visibility_of_element_located((self.home_page.headphons_category())))
        self.home_page.click_laptops()
        self.category_page.choose_product(1)
        self.product_page.input_quantity('4')
        self.product_page.click_add_cart()
        self.home_page.hover_icon_cart()
        self.assertEqual(self.home_page.total_products_icon_cart(),self.home_page.total_products_title())


    def test_3_remove_product_from_ucon_cart(self):
        # add first product to cart
        self.home_page.click_speakers()
        self.category_page.choose_product(1)
        self.product_page.click_add_cart()

        # add another product
        self.home_page.click_website_logo()
        self.home_page.click_speakers()
        self.category_page.choose_product(3)
        self.product_page.click_add_cart()
        self.home_page.hover_icon_cart()
        #the len of the list products before remove item
        len_before_remove= self.home_page.len_list_products_at_icon_cart()
        #remove item
        self.home_page.remove_product_icon_cart(1)
        self.assertNotEqual(len_before_remove, self.home_page.len_list_products_at_icon_cart())

    def test_4_go_shopping_cart_page(self):
        # add product to cart
        self.home_page.click_mice()
        self.category_page.choose_product(1)
        self.product_page.click_add_cart()
        self.home_page.hover_icon_cart()
        self.home_page.click_cart_icon()

        self.assertEqual(self.shopping_cart_page.shopping_card_text(),"SHOPPING CART")
