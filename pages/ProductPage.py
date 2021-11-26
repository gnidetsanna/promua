from selenium.webdriver.support.expected_conditions import element_to_be_selected
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

class ProductLocators:
    FAVORITE_BUTTON = (By.XPATH,'//*[@data-qaid = "add_favorite"]')
    FAVORITE_BUTTON_COUNTER = (By.XPATH,'//*[@data-qaid ="counter"]')


class Product_page(BasePage):

    def favorite_button(self):
        for i in range(0,12):
            self.find_element(ProductLocators.FAVORITE_BUTTON).click()

    def favorite_count(self):
        counter = self.find_element(ProductLocators.FAVORITE_BUTTON_COUNTER)
        if counter.text == "1":
            return True
        else:
            pass