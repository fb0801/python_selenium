from selenium import webdriver
import booking.constants as const
import os


class Booking(webdriver.Firefox):
    def __init__(self, teardown=False):
        #self.browser = webdriver.Chrome
        #self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__()
        #os.environ['PATH'] += self.driver_path
       
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, excel_tab):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, ):
        pass
        


