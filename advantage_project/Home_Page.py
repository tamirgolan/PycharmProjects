from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Home_Page:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def mice_category(self):
        return self.driver.find_element(By.ID, 'miceTxt')

    def click_mice(self):
        self.mice_category().click()

    def tablets_category(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[aria-label=TabletsCategoryTxt][class=shop_now_slider]")

    def click_tablets(self):
        self.tablets_category().click()

    def speakers_category(self):
        return self.driver.find_element(By.ID,'speakersTxt')

    def click_speakers(self):
        self.speakers_category().click()

    def laptops_category(self):
        return self.driver.find_element(By.ID,'laptopsTxt')

    def click_laptops(self):
        self.laptops_category().click()

    def headphons_category(self):
        return self.driver.find_element(By.ID,'headphonesLink')

    def click_headphons(self):
        self.headphons_category().click()

    def user_logo(self):
        return self.driver.find_element(By.ID,'hrefUserIcon')

    def click_user_logo(self):
        self.user_logo().click()

    def user_name(self):
        return self.driver.find_element(By.NAME, 'username')

    def input_user_name(self, user_name : str):
        self.user_name().send_keys(user_name)

    def password(self):
        return self.driver.find_element(By.NAME ,'password')

    def input_password(self, password : str):
        self.password().send_keys(password)

    def sign_in(self):
        return self.driver.find_element(By.ID, 'sign_in_btnundefined')

    def click_sign_in(self):
        self.sign_in().click()

    def create_new_account_button(self):
        return self.driver.find_element(By.CSS_SELECTOR ,"[translate=CREATE_NEW_ACCOUNT]")

    def click_create_new_account(self):
        self.create_new_account_button().click()

    def cart_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[aria-label='ShoppingCart']")

    def click_cart_icon(self):
        self.cart_icon().click()

    def hover_icon_cart(self):
        x = self.cart_icon()
        return ActionChains(self.driver).move_to_element(x).perform()

    def website_logo(self):
        return self.driver.find_element(By.CLASS_NAME ,'logo')

    def click_website_logo(self):
        self.website_logo().click()

    def search_icon(self):
        return self.driver.find_element(By.ID ,'menuSearch')

    def click_search_icon(self):
        self.search_icon().click()

    def search_line(self):
        return self.driver.find_element(By.ID,'autoComplete')

    def input_search_line(self, text: str):
        self.search_line().send_keys(text)

    def total_products_icon_cart(self):
        list_product = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")
        x = 0
        list_qty = []
        for i in range(len(list_product)):
            x += 1
            qty = self.driver.find_element(By.XPATH,f"//ul/li[2]/ul/li/tool-tip-cart/div/table/tbody/tr[{x}]/td[2]/a/label")
            num = qty.text.replace('QTY:', '')
            frisrttt = int(num)
            list_qty.append(frisrttt)
        return sum(list_qty)

    def total_products_title(self):
        title = self.driver.find_elements(By.CSS_SELECTOR, "[class='roboto-regular ng-binding']")
        qt = title[0].text
        num = qt.replace('Items)', '')
        quntity_title = num[1:]
        quntity_title = int(quntity_title)
        return quntity_title

    #def total_price_product_icon_cart(self):
       # self.driver.

    def remove_product_icon_cart(self,num_product_from1):
        self.remove= self.driver.find_elements(By.CSS_SELECTOR,"[class='removeProduct iconCss iconX']")
        num_product_from1-= 1
        self.remove[num_product_from1].click()

    # len of the list products in icon cart
    def len_list_products_at_icon_cart(self):
        self.list_products = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")
        return len(self.list_products)

    #all the details of products in ucon cart
    def products_details_in_icon_cart(self):
        self.products_details = self.driver.find_element(By.CSS_SELECTOR, "table>tbody>tr")
        return self.products_details

    def contact_us_text(self):
        self.contact_text = self.driver.find_elements(By.CSS_SELECTOR, "[class='menu navLinks roboto-regular ng-scope']")
        return self.contact_text[0].text

    def line_menu(self):
        self.line = self.driver.find_elements(By.CSS_SELECTOR, "[class='menu navLinks roboto-regular ng-scope']")

