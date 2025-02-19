from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from booking.booking_filtrations import BookingFiltration


class Booking(webdriver.Firefox):
    def __init__(self, teardown=False):
        
        self.teardown = teardown
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(15)  # Apply implicit wait
        self.browser.maximize_window()  # Maximize browser window

    

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Ensures the browser closes when exiting the context.
        """
        if self.teardown:
            self.browser.quit()

    def land_first_page(self):
        """
        Opens the base URL.
        """
        self.browser.get(const.BASE_URL)  # Use self.driver to call get()

    def change_currency(self, currency=None):
        currency_element = self.browser.find_element(By.CSS_SELECTOR, 
                'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.browser.find_element(By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'                                              
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_feild = self.browser.find_element(By.ID, 'ss')
        search_feild.clear()
        search_feild.send_keys(place_to_go)

        first_result = self.browser.find_element(By.CSS_SELECTOR, 
                'li[data-i="0"]'
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.browser.find_element(By.CSS_SELECTOR, 
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.browser.find_element(By.CSS_SELECTOR, 
               f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self, count):
        selection_element = self.browser.find_element(By.ID, 'xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.browser.find_element(By.CSS_SELECTOR, 
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()

            adults_value_element = self.browser.find_element(By.ID, 'group_adults')
            adults_value = adults_value_element.get_attribute(
                'value') #give adult count
            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(By.CSS_SELECTOR,
            'button[aria-label="Increase number of adults"]' 
        )

        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]'                                  
        )
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)