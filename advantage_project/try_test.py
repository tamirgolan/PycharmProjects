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
driver.implicitly_wait(20)
home=Home_Page(driver)



a = driver.find_elements(By.CSS_SELECTOR, "[class='productName ng-binding']")
a[1].click()

text = driver.find_element(By.CSS_SELECTOR, " [class='roboto-regular screen768 ng-binding']")
print(text.text)

product = Product_Page(driver)
print(product.price_product_float())

qa= driver.find_element(By.CSS_SELECTOR, "[name = 'quantity']")
qa.clear()
qa.send_keys('2')
#באג בניקוי
#add product to cart
add=driver.find_element(By.NAME, "save_to_cart")
add.click()

#add another product to cart
web_logo = driver.find_element(By.CLASS_NAME ,'logo')
web_logo.click()

mice= driver.find_element(By.ID, 'miceTxt')
mice.click()

choose = driver.find_elements(By.CSS_SELECTOR, "[class='productName ng-binding']")
choose[1].click()

add=driver.find_element(By.NAME, "save_to_cart")
add.click()
#sleep(7)
#באגגגגג שמוסיפים 12

cart= driver.find_elements(By.CSS_SELECTOR,"[fill='#313131']")
c = driver.find_element(By.CSS_SELECTOR,"[aria-label='ShoppingCart']")

#ריחוףףףף
ActionChains(driver).move_to_element(c).perform()
#משיכת כמויות = דינאמי

title = driver.find_elements(By.CSS_SELECTOR,"[class='roboto-regular ng-binding']")
qt = title[0].text
num = qt.replace('Items)', '')
quntity_title = num[1:]
quntity_title = int(quntity_title)

print(home.len_list_products_at_icon_cart())


products_details = driver.find_element(By.CSS_SELECTOR, "table>tbody>tr")
list_products_details = []
#for i in range(len(list_products)):
  #  print(list_products[i].text)



    #list_products_details.append(list_products[i].text)
    #print(list_products_details)


#print(len(list_products))
#הוצאת מחירים מאייקון עגלה

home.click_website_logo()
list_price = driver.find_elements(By.CSS_SELECTOR,"[class='price roboto-regular ng-binding']")
new_list = []
for i in range(len(list_price)):
    new_list.append(list_price[i].text)

#for i in range(len(new_list)):

#   num = new_list.replace('$', "")

print(new_list)
print(num)






print(home.total_products_title())
print(home.total_products_icon_cart())


#qu1 = qu.text.replace("QTY:","")

#qu2 = int(qu1)

#qu = driver.find_elements(By.XPATH,"//table/tbody/tr/td[2]/a/label")
#qu= list(qu)
#for i in range(len(qu)):
   # qu[i] = qu[i].text

#print(qu)

# QTY1=qu.tex

home.click_cart_icon()
sleep(2)

list = driver.find_element(By.CSS_SELECTOR, "tbody>tr>td>label")
print("!!!!")
print(list.text)