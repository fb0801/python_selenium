from selenium import webdriver
import booking.constants as const
import os


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"", teardown=False):
        self.driver_path = driver_path
        super(Booking, self).__init__()
        os.environ['PATH'] += self.driver_path

    def __exit__(self, exc_type, exc_val, excel_tab):
        if self.teradown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        


