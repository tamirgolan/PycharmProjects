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


service_chrome = Service(r"C:\selenium1\chromedriver.exe")

# Open browser (create a driver object)
driver = webdriver.Chrome(service=service_chrome)

# Go to the required URL
driver.get("https://advantageonlineshopping.com/#/category/Speakers/4")

driver.maximize_window()
driver.implicitly_wait(10)
home=Home_Page(driver)

home.click_website_logo()
sleep(3)

print(home.contact_us_text())