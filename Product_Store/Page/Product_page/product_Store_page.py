import time
from selenium.webdriver.common.by import By
from Product_Store.Base.Base_test.Product_Store_Base import BaseTest
from Product_Store.Locaters.Product_Store_locaters.all_product_locaters import Locators


class ProductStore(BaseTest, Locators):
    def open(self):
        self._driver.get(self.url)
        self._driver.maximize_window()

    def execute_home_icon(self):
        self._click(By.XPATH, self.home_icon_xpath)
        self._click(By.XPATH, self.catagories_xpath)
        self._click(By.XPATH, self.phone_xpath)
        self._click(By.XPATH, self.s6_xpath)
        self._click(By.XPATH, self.add_to_cart_xpath)
        assert self.check_product(self.name_assert_xpth) == "Samsung galaxy s6"
        self._click(By.XPATH, self.cart_icon_xpath)
        self._click(By.XPATH, self.a_xpath)
        self._click(By.XPATH, self.B_xpath)
        self._click(By.XPATH, self.c_xpath)
        self._click(By.XPATH, self.place_order_xpath)
        self._click(By.XPATH, self.place_order_xpath1)
        self._click(By.XPATH, self.total_xpath)
        self._write(By.XPATH, self.Name_xpath, 'Temesgen')
        self._write(By.XPATH, self.country_xpath, 'Israel')
        self._write(By.XPATH, self.city_xpath, 'Bear_Shava')
        self._write(By.XPATH, self.card_xpath, '123456')
        self._write(By.XPATH, self.month_xpath, '01')
        self._write(By.XPATH, self.year_xpath, '2023')
        self._click(By.XPATH, self.purchase_xpath)
        self._click(By.XPATH, self.ok_expath)

    def execute_contact_icon(self):
        self._click(By.XPATH, self.contact_icon_expth)
        self._click(By.XPATH, self.contact_email_expath1)
        self._write(By.XPATH, self.contact_email_expath, 'tasmamaw52@gmail.com')
        self._write(By.XPATH, self.contact_name_expath, 'Temesgen')
        self._write(By.XPATH, self.Message_expath, 'There is A problem on the phone')
        self._click(By.XPATH, self.send_massage_expath)

    def execute_about_us_icon(self):
        self._click(By.XPATH, self.about_us)
        self._click(By.XPATH, self.about_us_body_xpath)
        self._click(By.XPATH, self.about_us_vedio)
        self._click(By.XPATH, self.about_us_vedio_play_xpath)
        self._click(By.XPATH, self.about_us_close_xpath)

    def execute_login_icon(self):
        self._click(By.XPATH, self.login_xpath)
        self._click(By.XPATH, self.login_header_xpath)
        self._click(By.XPATH, self.login_username_body_xpath)
        self._write(By.XPATH, self.user_name_field_xpath, 'Temasm')
        self._write(By.XPATH, self.password_field_xpath, '12345')
        self._click(By.XPATH, self.login_footer_xpath)
        self._click(By.XPATH, self.login_button_expath)

    def execute_sign_up(self):
        self._click(By.XPATH, self.sign_up_icon_xpath)
        self._click(By.XPATH, self.sign_up_header_xpath)
        self._write(By.XPATH, self.sign_up_username_xpath, 'Temasm')
        self._write(By.XPATH, self.sign_up_password_xpath, '12345')
        self._click(By.XPATH, self.sign_up_footer_xpath)
        self._click(By.XPATH, self.sign_up_xpath)

    def execute_categories_icon(self):
        self._click(By.XPATH, self.catagories_xpath)

    def execute_phone_categories(self):
        self._click(By.XPATH, self.phone_category_xpath)

    def execute_laptops_categories(self):
        self._click(By.XPATH, self.laptops_category_xpath)

    def execute_monitors_categories(self):
        self._driver.execute_script("window.scrollBy(0,5000);")
        self._driver.find_element(By.XPATH,"//a[contains(text(),'Monitors')]").click()

    def execute_scroll(self):  # How to scroll down to the next page
        self._click(By.XPATH, self.home_icon_xpath)
        self._driver.execute_script("window.scrollBy(0,3000);")
        self._driver.find_element(By.XPATH,"/html[1]/body[1]/div[5]/div[1]/div[2]/form[1]/ul[1]/li[2]/button[1]").click()
