#methods to parse data we need 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self, boxes_section_element):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_element(By.CLASS_NAME,
         'sr_property_block')