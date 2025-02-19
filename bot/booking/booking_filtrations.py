#class with inst to interact with application with results
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, drvier:WebDriver):
        self.driver = drvier

    def apply_star_rating(self, *star_value):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR,
            'filter_class'                                  
        )
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, 
            '*'
        )
        
        for star_element in star_child_elements:
            if (star_element.get_attribute("innerHTML")).strip() == f'{star_value} stars':
                star_element.click()