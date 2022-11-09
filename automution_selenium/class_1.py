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

#sleep(5) #לומר לתוכנית להיות בשהייה 5 שניות
#driver.close() #סגירת דפדפן

driver.get("https://www.google.co.il/")
driver.maximize_window()
#מגדירים פעם בתוכנית
driver.implicitly_wait(10)

# get the gmail title element:
gmail_element = driver.find_element(By.CSS_SELECTOR, "#gb > div > div:nth-child(1) > div > div:nth-child(1) > a")

if gmail_element.text=='Gmail':
    print('test 1 passed')
else:
    print(f"test faild. Expected : Gmail .  Acyual: {gmail_element.text}")
search_line = driver.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")


search_line.send_keys("selenium")
sleep(0.4)
search_line.clear()

search_line.send_keys("java")
sleep(0.4)
search_line.clear()

search_line.send_keys("python")
#press - click:
#driver.find_element(By.CSS_SELECTOR, " body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b").click()

# press - Enter:
search_line.send_keys(Keys.ENTER)
#back:
#driver.back()

#בדיקה שבאמת כתוב "פייתון" בשורת חיפוש

search_line2 = driver.find_element(By.CSS_SELECTOR , "#tsf > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
value = search_line2.get_attribute("value")

if value == "python":
    print("test 2 passed")
else:
    print(f"test faild. Expected: python actual:{value}")




sleep(1)
driver.close()
