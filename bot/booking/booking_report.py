#methods to parse data we need 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CLASS_NAME,
         'sr_property_block')
    
    def pull_deal_box_attributes(self):
        collection = []
        #pull hotel name
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(By.CLASS_NAME,
                'sr-hotel__name').get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element(By.CLASS_NAME,
                 'bui-price-display__value').get_attribute('innerHTML').strip()
            hotel_score = deal_box.get_attribute(
                'data-score'
            ).strip()

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection