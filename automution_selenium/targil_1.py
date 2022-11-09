from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#בשביל אנטר!
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_chrome = Service(r"C:\selenium1\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)
driver.maximize_window()
driver.get("https://phptravels.net/api/admin")
driver.implicitly_wait(10)

gmail_element = driver.find_element(By.CSS_SELECTOR, "[name='email'][type='text']")
passworld_element = driver.find_element(By.CSS_SELECTOR,"[name='password']")
login_element = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
gmail_element.send_keys('admin@phptravels.com')
passworld_element.send_keys('demoadmin')
login_element.click()


dashboard_element = driver.find_element(By.CSS_SELECTOR,"[class='text-uppercase font-monospace']")

if dashboard_element.text == "DASHBOARD":
    print("test 1 passed")
else:
    print("fail")

booking_element = driver.find_element(By.LINK_TEXT, 'Bookings')
booking_element.click()

account_element = driver.find_element(By.CSS_SELECTOR,"[id='dropdownMenuProfile']")
account_element.click()
sleep(0.2)
#ברבים כי מצפים לקבל רשימה elements
#logout
list_menu_option = driver.find_elements(By.CSS_SELECTOR,".dropdown-item>.me-3")

while True:
    try:
        list_menu_option[3].click()
        break
    except:
        continue

wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".display-5")))


