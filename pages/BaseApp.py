from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://prom.ua/Velosipednye-shiny"
        self.product_url = "https://prom.ua/p712545800-pokrishka-schwalbe-marathon.html"
        self.favorite_url = "https://my.prom.ua/cabinet/user/favorites"

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_product_url(self):
        return self.driver.get(self.product_url)

    def go_to_favorite_url(self):
        return self.driver.get(self.favorite_url)