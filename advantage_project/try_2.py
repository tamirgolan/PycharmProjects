from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Home_Page import Home_Page
from Product_Page import Product_Page
from Category_Page import Category_Page


service_chrome = Service(r"C:\selenium1\chromedriver.exe")

# Open browser (create a driver object)
driver = webdriver.Chrome(service=service_chrome)

# Go to the required URL
driver.get("https://advantageonlineshopping.com/#/category/Speakers/4")

driver.maximize_window()
driver.implicitly_wait(10)
home=Home_Page(driver)

home.click_website_logo()

home.click_mice()
product = Product_Page(driver)
category = Category_Page(driver)

category.choose_product(3)
product.choose_color_click(2)
product.click_add_cart()
x = driver.find_elements(By.CSS_SELECTOR, "[id='rabbit']")
print(x[0].get_attribute("title"))

name = product.name_product()
print(name)
print(len(name))

home.click_website_logo()
home.click_headphons()