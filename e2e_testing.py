from selenium import webdriver
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tests.Home_Page import HomePage
from utilities.BaseClass import BaseClass


class TestGoogle(BaseClass):
    def test_e2e(self):
        homepage = HomePage(self.driver)
        checkout_page = homepage.shop_items()
        checkout_page.add_to_cart().click()
        checkout_page.primary_check_out_item().click()
        confirm_page = checkout_page.success_check_out()
        confirm_page.enter_country_name().send_keys("ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        confirm_page.select_country().click()
        confirm_page.get_checkbox_clicked().click()
        confirm_page.submit_order().click()
        success_text = confirm_page.get_success_message().text

        assert "Success!ertyui Thank you!" in success_text

        self.driver.get_screenshot_as_file("screen.png")
        self.driver.get_screenshot_as_file("screen.png")
        self.driver.get_screenshot_as_file("screen.png")