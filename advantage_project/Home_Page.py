from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from re import sub


class Home_Page:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def mice_category(self):
        return self.driver.find_element(By.ID, 'miceTxt')

    # click on mice category
    def click_mice(self):
        self.mice_category().click()

    # click on tablets category
    def tablets_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[aria-label=TabletsCategoryTxt][class=shop_now_slider]")

    # click on tablets category
    def click_tablets(self):
        self.tablets_category().click()

    def speakers_category(self):
        return self.driver.find_element(By.ID, 'speakersTxt')

    # click on speakers category
    def click_speakers(self):
        self.speakers_category().click()

    def laptops_category(self):
        return self.driver.find_element(By.ID, 'laptopsTxt')

    # click on laptops category
    def click_laptops(self):
        self.laptops_category().click()

    def headphons_category(self):
        return self.driver.find_element(By.ID, 'headphonesTxt')

    # click on headphones category
    def click_headphons(self):
        self.headphons_category().click()

    def user_logo(self):
        return self.driver.find_element(By.ID, 'hrefUserIcon')

    # click on user logo
    def click_user_logo(self):
        self.user_logo().click()

    def user_name(self):
        return self.driver.find_element(By.NAME, 'username')

    def input_user_name(self, user_name: str):
        self.user_name().send_keys(user_name)

    def password(self):
        return self.driver.find_element(By.NAME, 'password')

    def input_password(self, password: str):
        self.password().send_keys(password)

    def sign_in(self):
        return self.driver.find_element(By.ID, 'sign_in_btnundefined')

    def click_sign_in(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'sign_in_btnundefined'))).click()

    def create_new_account_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[translate=CREATE_NEW_ACCOUNT]")

    def click_create_new_account(self):
        self.create_new_account_button().click()

    def cart_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[aria-label='ShoppingCart']")

    def click_cart_icon(self):
        self.cart_icon().click()

    # hover on icon cart from any screen
    def hover_icon_cart(self):
        x = self.cart_icon()
        return ActionChains(self.driver).move_to_element(x).perform()

    def website_logo(self):
        return self.driver.find_element(By.CLASS_NAME, 'logo')

    # click on website logo from any screen
    def click_website_logo(self):
        self.website_logo().click()

    def search_icon(self):
        return self.driver.find_element(By.ID, 'menuSearch')

    def click_search_icon(self):
        self.search_icon().click()

    def search_line(self):
        return self.driver.find_element(By.ID, 'autoComplete')

    def input_search_line(self, text: str):
        self.search_line().send_keys(text)

    # return the total products in icon cart (sum)
    def total_products_icon_cart(self):
        list_product = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")
        x = 0
        list_qty = []
        for i in range(len(list_product)):
            x += 1
            qty = self.driver.find_element(By.XPATH,
                                           f"//ul/li[2]/ul/li/tool-tip-cart/div/table/tbody/tr[{x}]/td[2]/a/label")
            num = qty.text.replace('QTY:', '')
            frisrttt = int(num)
            list_qty.append(frisrttt)
        return sum(list_qty)

    # return the QTY in icon cart - title
    def total_products_title(self):
        title = self.driver.find_elements(By.CSS_SELECTOR, "[class='roboto-regular ng-binding']")
        qt = title[0].text
        num = qt.replace('Items)', '')
        quntity_title = num[1:]
        quntity_title = int(quntity_title)
        return quntity_title

    # choose a number of product in icon cart - the first product is 1 and remove him
    def remove_product_icon_cart(self, num_product_from1):
        self.remove = self.driver.find_elements(By.CSS_SELECTOR, "[class='removeProduct iconCss iconX']")
        num_product_from1 -= 1
        self.remove[num_product_from1].click()

    # len of the list products in icon cart
    def len_list_products_at_icon_cart(self):
        self.list_products = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")
        return len(self.list_products)

    # all the details of products in ucon cart
    def products_details_in_icon_cart(self):
        self.products_details = self.driver.find_element(By.CSS_SELECTOR, "table>tbody>tr")
        return self.products_details

    # return the "contact us" (in the home page - line menu)
    def contact_us_text(self):
        # self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[ng-show='welcome']")))
        y = self.driver.find_elements(By.CSS_SELECTOR, "[class='menu navLinks roboto-regular ng-scope']")
        text = y[0].text
        return text

    # return the color of product
    def color_product_icon_cart(self, num_product_from1: int):
        num_product_from1 -= 1
        color = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a>label>span")
        color = color[num_product_from1].text
        return color

    # return the name of product that in icon cart , choose a number of product - first product is "1" - "user friendly"
    def name_product_icon_cart(self, num_of_product_from1: int):
        num_of_product_from1 -= 1
        self.name_product = self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr>td>a>h3")
        return self.name_product[num_of_product_from1].text

    # return the QTY of product that in icon cart , choose a number of product -  first product is "1" - "user friendly"
    def qty_of_product_icon_cart(self, num_of_product_from1: int):
        num_of_product_from1 -= 1
        qty = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/a/label[1]")
        qty = qty[num_of_product_from1].text
        qty = qty[4:]
        qty = int(qty)
        return qty

    # return the price of product that in icon cart , choose a number of product -  first product is "1" - "user friendly"

    def price_of_product_icon_cart(self, num_of_product_from1: int):
        num_of_product_from1 -= 1
        price = self.driver.find_elements(By.CSS_SELECTOR, "[class='price roboto-regular ng-binding']")
        price = price[num_of_product_from1].text
        price = price[1:]
        price1 = price = float(sub(r'[^\d.]', '', price))
        return price1

    def user_icon_after_log_in_TG(self):
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[class='hi-user containMiniTitle ng-binding']"))).click()

    def user_log_out_bottun_TG(self):
        self.log_out_bottun = self.driver.find_elements(By.CSS_SELECTOR, "#menuUserLink>div>label")
        self.log_out_bottun[2].click()

    def equal_name_after_log_out(self):
        self.name_on = self.driver.find_element(By.CSS_SELECTOR, "[class='hi-user containMiniTitle ng-binding']")
        return self.name_on.text

    def regist_un(self, txt):
        self.userssr = self.driver.find_element(By.NAME, "usernameRegisterPage")
        self.userssr.send_keys(txt)

    # def send_user(self, txt):
    #     self.userssr.send_keys(txt)

    def regist_pass_word(self, txt: str):
        self.Pass = self.driver.find_element(By.NAME, "passwordRegisterPage")
        self.Pass.send_keys(txt)

    def confirm_password(self, txt: str):
        self.Pass = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
        self.Pass.send_keys(txt)

    def send_email(self, txt: str):
        self.email = self.driver.find_element(By.NAME, "emailRegisterPage")
        self.email.send_keys(txt)

    def create_radio_bottun(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "i_agree"))).click()
        # self.radioBB=self.wait.untilself.driver.find_element(By.NAME,"i_agree").click()



    def click_create_action(self):
        self.driver.find_element(By.ID, "register_btnundefined").click()

        # self.driver.execute_script("arguments[0].click();", click)

        def click_create_click(self):
            click_b = self.driver.find_element(By.ID, "register_btnundefined")
            click_b.click()

        def click_create_BY_CLASS(self):
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sec-sender-a ng-scope"))).click()

        # def click_create_2(self):
        #     create=self.wait.until(EC.visibility_of_element_located((By.ID,"[class='sec-sender-a ng-scope'][id='register_btnundefined']"))).click()
        #     create.click()

    # self.create_bottun=self.driver.find_element(By.ID,"register_btnundefined").click()
