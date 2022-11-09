from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

service_chrome = Service(r"C:\selenium1\chromedriver.exe")

# Open browser (create a driver object)
driver = webdriver.Chrome(service=service_chrome)

# Go to the required URL
driver.get("https://juliemr.github.io/protractor-demo/")

driver.maximize_window()
driver.implicitly_wait(10)

first_num_list=[10,11,12]
second_num_list=[2,3,4]
op_list=["+","-","/"]

first_num = driver.find_element(By.CSS_SELECTOR,"[ng-model='first']")
operator = driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")
op_dropdown = Select(operator)
second_num = driver.find_element(By.CSS_SELECTOR,"[ng-model='second']")
go = driver.find_element(By.CSS_SELECTOR,"#gobutton")

for i in range(3):
    # Type first number
    first_num.send_keys(first_num_list[i])

    # Choose operator
    op_dropdown = Select(operator)
    op_dropdown.select_by_visible_text(op_list[i])

    # Type second number
    second_num.send_keys(second_num_list[i])

    # Click Go
    go.click()

    # Check the result
    result = driver.find_element(By.CSS_SELECTOR,"h2.ng-binding")

    while result.text[0]=='.':
        pass

# Print the history table

# Find the table element
table = driver.find_element(By.CLASS_NAME,"table")

rows = table.find_elements(By.TAG_NAME,"tr")

for row in rows[1:]:
    cols = row.find_elements(By.TAG_NAME,"td")
    for col in cols:
        print(col.text, end="\t")
    print()

first_num.send_keys(22)
second_num.send_keys(10)
go.click()


