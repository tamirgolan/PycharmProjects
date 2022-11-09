from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_chrome = Service(r"C:\selenium1\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome, options=chrome_options)
driver.maximize_window()
driver.get("https://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10)

#click on flight

flights = driver.find_element(By.LINK_TEXT,'Flights')
flights.click()

#check that rount trip is on
round_trip_radio = driver.find_element(By.CSS_SELECTOR, "input[value='roundtrip']")
if round_trip_radio.is_selected():
    print('test 1 passed')
else:
    print('test 1 faild')

# passengers check default:

passengers = driver.find_element(By.NAME, "passCount")
value = passengers.get_attribute("value")
if value== '1':
    print('test 2 passed')
else:
    print('test 2 faild')

#בחירה מתוך דרופ ליסט על ידי שימוש ב SELECT

departing_from = driver.find_element(By.NAME,"fromPort")
passengers_dropdown = Select(passengers)
passengers_dropdown.select_by_visible_text('2')
sleep(1)
#choose month:
month = driver.find_element(By.NAME, "fromMonth")
month_dropdown = Select(month)
month_dropdown.select_by_value('8')
sleep(1)
#drop down object to departing_from - london:

departing_from_dropdown = Select(departing_from)
departing_from_dropdown.select_by_index(2)
sleep(1)

driver.close()