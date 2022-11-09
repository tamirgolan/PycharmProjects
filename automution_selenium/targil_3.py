from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_chrome = Service(r"C:\selenium1\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome, options=chrome_options)
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10)

user_name = driver.find_element(By.CSS_SELECTOR,"[name='userName']")
user_name.send_keys('tutorial')

password = driver.find_element(By.CSS_SELECTOR,"[name='password']")
password.send_keys('tutorial')

login = driver.find_element(By.CSS_SELECTOR," [name='submit']")
login.click()

flights = driver.find_element(By.LINK_TEXT,'Flights')
flights.click()

one_way = driver.find_element(By.CSS_SELECTOR,"[name='tripType'][value='roundtrip']" )
one_way.click()

economy = driver.find_element(By.CSS_SELECTOR, " [name='servClass'][value='Coach']")
economy.click()

continue_element = driver.find_element(By.CSS_SELECTOR, " [name='findFlights']")
continue_element.click()



sleep(0.5)
driver.close()