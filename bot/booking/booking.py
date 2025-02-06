from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Booking:
    def __init__(self, teardown=False):
        
        self.driver = webdriver.Firefox()
        self.teardown = teardown
        
       
        self.driver.implicitly_wait(15)  # Apply implicit wait
        self.driver.maximize_window()  # Maximize browser window

    def __exit__(self, exc_type, exc_val, excel_tab):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.driver.find_element(By.CSS_SELECTOR, 
                'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        
