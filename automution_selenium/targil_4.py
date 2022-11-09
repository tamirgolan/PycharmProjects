from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service_chrome = Service(r"C:\selenium1\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)
driver.maximize_window()
driver.get("https://juliemr.github.io/protractor-demo/")
driver.implicitly_wait(10)

number_1 = driver.find_element(By.CSS_SELECTOR, "[ng-model='first']")
number_2 = driver.find_element(By.CSS_SELECTOR, "[ng-model='second']")
action_math = driver.find_element(By.CSS_SELECTOR, "[ng-model='operator']")
go_button = driver.find_element(By.ID, "gobutton")

number_2.send_keys(22)
number_1.send_keys(10)
action_math_drop_down = Select(action_math)
action_math_drop_down.select_by_value("MULTIPLICATION")
sleep(1)
go_button.click()
sleep(1)

result = driver.find_element(By.CSS_SELECTOR, "[class='ng-binding']")
#while result.text[0]=='.':
   # pass
#שימוש ב wait לטובת המתנה עד ש...
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"td.ng-binding")))





if result.text == '220':
    print('test 1 passed')
else:
    print('test 1 faild')


