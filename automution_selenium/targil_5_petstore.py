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
driver.get("https://petstore.octoperf.com/actions/Catalog.action")
driver.implicitly_wait(10)

category_animal = driver.find_elements(By.CSS_SELECTOR, "#SidebarContent>a>img")
category_animal[0].click()

category_fish = driver.find_elements(By.CSS_SELECTOR, "td>a")
category_fish[0].click()

anglefish = driver.find_elements(By.CSS_SELECTOR, "[class='Button']")
anglefish[0].click()


quantity = driver.find_element(By.CSS_SELECTOR, "[value='1']")
quantity.clear()
quantity.send_keys('3')

update_card_button = driver.find_element(By.CSS_SELECTOR, "[name='updateCartQuantities'] ")
update_card_button.click()

return_home_page = driver.find_element(By.ID, "BackLink")
return_home_page.click()

category_animal = driver.find_elements(By.CSS_SELECTOR, "#SidebarContent>a>img")
category_animal[0].click()

category_fish = driver.find_elements(By.CSS_SELECTOR, "td>a")
category_fish[1].click()

add_cart = driver.find_element(By.LINK_TEXT,"Add to Cart")
add_cart.click()

quantity_1 = driver.find_element(By.CSS_SELECTOR, "[name='EST-1']")
quantity_2 = driver.find_element(By.CSS_SELECTOR, "[name='EST-3'] ")

td = driver.find_elements(By.CSS_SELECTOR,"form>table>tbody>tr>td")
list_price_1 = td[5]
list_price_2 = td[13]


price1 = float(list_price_1.text[1:])

price2 = float(list_price_2.text[1:])

quantity1 = driver.find_element(By.CSS_SELECTOR, "[name='EST-1']")
value1 = quantity1.get_attribute("value")
value1=int(value1)

quantity2 = driver.find_element(By.CSS_SELECTOR, "[name='EST-3'] ")
value2 = quantity2.get_attribute("value")
value2=int(value2)

total_price_1 = td[6].text
total_1 = float(total_price_1[1:])

total_price_2 = td[14].text
total_2 = float(total_price_2[1:])

if total_1 == price1*value1:
    print("test 1 passed")
else:
    print(f"test 1 faild")

if total_2 == price2 * value2:
    print("test 2 passed")
else:
    print("test 2 faild")

sub_total = driver.find_element(By.CSS_SELECTOR,"[colspan='7']")
total = float(sub_total.text[12:])

if total== (price1*value1) + (price2*value2):
    print('test 3 passed')
else:
    print('test 3 faild')

return_home_page = driver.find_element(By.ID, "BackLink")
return_home_page.click()

category_animal = driver.find_elements(By.CSS_SELECTOR, "#SidebarContent>a>img")
category_animal[1].click()

dogs_category = driver.find_elements(By.CSS_SELECTOR,"tr>td>a")
dogs_category[1].click()

add_cart = driver.find_element(By.CSS_SELECTOR, "[class='Button']")
add_cart.click()

update_card_button = driver.find_element(By.CSS_SELECTOR, "[name='updateCartQuantities'] ")
update_card_button.click()


sleep(4)