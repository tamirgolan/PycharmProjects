from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from CalcPage import CalcPage


service_chrome = Service(r"C:\selenium1\chromedriver.exe")

# Open browser (create a driver object)
driver = webdriver.Chrome(service=service_chrome)

# Go to the required URL
driver.get("https://juliemr.github.io/protractor-demo/")

driver.maximize_window()
driver.implicitly_wait(10)

#create object
calc_page = CalcPage(driver)
# 12* 3 and check:

calc_page.type_num1('12')
calc_page.type_num2('3')
calc_page.choose_op('*')
calc_page.go_click()

if calc_page.final_result_text() == '36':

    print('test passed')
else:
    print(f'test faild , actual : {calc_page.final_result_text()}')
