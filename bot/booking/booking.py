from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Booking:
    def __init__(self, teardown=False):
        
        self.teardown = teardown
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)  # Apply implicit wait
        self.driver.maximize_window()  # Maximize browser window

    

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Ensures the browser closes when exiting the context.
        """
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        """
        Opens the base URL.
        """
        self.driver.get(const.BASE_URL)  # Use self.driver to call get()

    def change_currency(self, currency=None):
        currency_element = self.driver.find_element(By.CSS_SELECTOR, 
                'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.driver.find_element(By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'                                              
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_feild = self.driver.find_element(By.ID, 'ss')
        search_feild.clear()