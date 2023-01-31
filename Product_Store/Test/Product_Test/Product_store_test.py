import allure
import pytest

from Product_Store.Page.Product_page.product_Store_page import ProductStore


class Test_Product_Stores(ProductStore):

    @allure.description('home page clikable')
    @pytest.mark.sanity
    def test_home_icon_clickable(self):
        access = ProductStore()
        access.open()
        access.execute_home_icon()

    def test_contact_icon_clickable(self):
        access = ProductStore()
        access.open()
        access.execute_contact_icon()

    def test_about_us(self):
        access = ProductStore()
        access.open()
        access.execute_about_us_icon()

    def test_login_clickable(self):
        access = ProductStore()
        access.open()
        access.execute_login_icon()

    def test_sign_up(self):
        access = ProductStore()
        access.open()
        access.execute_sign_up()

    def test_categories_clickable(self):
        access = ProductStore()
        access.open()
        access.execute_categories_icon()

    def test_phone_categories_clickable(self):
        access = ProductStore()
        access.open()
        access.execute_phone_categories()

    def test_laptops_categories_clickable(self):
        access = ProductStore()
        access.open()
        access.execute_phone_categories()

    def test_monitors_categories_clickable(self):
        access = ProductStore()
        access.open()
        access.execute_phone_categories()



    def test_scroll(self):
        access = ProductStore()
        access.open()
        access.execute_scroll()