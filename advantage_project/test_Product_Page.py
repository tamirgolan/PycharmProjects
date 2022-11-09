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
        self.product_page.click_add_cart()
        #add another product
        self.home_page.click_website_logo()

        #self.wait.until(EC.visibility_of_element_located((self.home_page.headphons_category())))
        self.home_page.click_laptops()
        self.category_page.choose_product(1)
        self.product_page.input_quantity('4')
        self.product_page.click_add_cart()
        self.home_page.hover_icon_cart()
        self.assertEqual(self.home_page.total_products_icon_cart(),self.home_page.total_products_title())

    def test_2(self):
        pass


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
        #if have the text "SHOPPING CART", and the element -  that we in correctly page
        self.assertEqual(self.shopping_cart_page.shopping_card_text(),"SHOPPING CART")

    def test_5(self):
        pass


    def test_6(self):
        # add product to cart
        self.home_page.click_mice()
        self.category_page.choose_product(2)
        self.product_page.input_quantity('3')
        self.product_page.click_add_cart()
        #add another product
        self.home_page.click_website_logo()
        self.home_page.click_speakers()
        self.category_page.choose_product(1)
        self.product_page.input_quantity('2')
        self.product_page.click_add_cart()
        #go to shopping cart page
        self.home_page.hover_icon_cart()
        self.home_page.click_cart_icon()
        #edit first product (QTY) , from QTY: 2 to QTY: 4
        self.shopping_cart_page.click_edit_product(1)
        qty_product1 = '4'
        self.product_page.input_quantity(qty_product1)
        self.product_page.click_add_cart()
        qty_product1 = int(qty_product1)
        #test to the first product. the qty need to be equal to the edit change
        self.assertEqual(qty_product1,self.shopping_cart_page.qty_first_product_shipping_page())

        #edit the QTY of second product, from QTY: 3 TO QTY: 5
        qty_product2= '5'
        self.home_page.click_cart_icon()
        self.shopping_cart_page.click_edit_product(2)
        self.product_page.input_quantity(qty_product2)
        self.product_page.click_add_cart()
        self.home_page.click_cart_icon()
        qty_product2 = int(qty_product2)

        #test to the second product. the qty need to be equal to the edit change.
        self.assertEqual(qty_product2,self.shopping_cart_page.qty_second_product_shipping_page())
        #end test to first product. the qty need to stay equal after changes in second product
        self.assertEqual(qty_product1,self.shopping_cart_page.qty_first_product_shipping_page())
######## have bug : When you edit the quantity of the second product, it changes the quantity for the first product  ######























    def test_7_back_from_TABLET(self):
        # add product to cart from tablet category
        self.home_page.click_tablets()
        self.category_page.choose_product(1)
        self.product_page.click_add_cart()
        #back to tablet category
        self.driver.back()
        #check if the category tablet was open
        self.assertEqual(self.category_page.name_category(),"TABLETS")
        #back to home page
        self.driver.back()
        #check if the home page was open
        #self.wait.until(EC.visibility_of_element_located((self.home_page.line_menu()[0])))
        #sleep(2)
        self.assertEqual(self.home_page.contact_us_text(),"CONTACT US")










    def test_8(self):
        pass

    def test_9(self):
        pass


    def test_10(self):
        pass


