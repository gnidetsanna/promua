from selenium.webdriver.support.expected_conditions import element_to_be_selected
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class PromSeacrhLocators:

    LOGIN_BUTTON = (By.XPATH,'//*[@data-qaid="sign-in"]')
    EMAIL_BUTTON = (By.XPATH, '//*[@data-qaid="email_btn"]')
    USER_LOGIN_FIELD = (By.XPATH,'//*[@id="email_field"]')
    DALI_BUTTON = (By.XPATH,'//*[@id="emailConfirmButton"]')
    PASSWORD_FIELD = (By.XPATH,'//*[@id="enterPassword"]')
    DALI_2_BUTTON = (By.XPATH,'//*[@id="enterPasswordConfirmButton"]')

    SEARCH_FIELD = (By.XPATH,'//*[@id="page-block"]/div/header/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div/div[2]/div/input')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="page-block"]/div/header/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/form/div/div[5]/button')

    PRODUCT_CARDS_MENU = (By.XPATH,'//*[@id="page-block"]/div/div[4]/div/div[3]/div[2]/div/div[2]/div[1]')
    PRODUCT_PRODUCER = (By.XPATH, '//*[@data-qaid="company_name"')
    TARGET_PRODUCER_NAME = (By.CSS_SELECTOR,"a.КРУТИ ПЕДАЛІ")

    PRODUCT_LINK_1 = (By.PARTIAL_LINK_TEXT,'pokrishka-schwalbe-marathon')
    PRODUCT_LINK = (By.PARTIAL_LINK_TEXT,'shopping_cart/add_item')


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(PromSeacrhLocators.LOCATOR_PROM_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(PromSeacrhLocators.LOCATOR_PROM_SEARCH_BUTTON,time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(PromSeacrhLocators.LOCATOR_PROM_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def login_button(self):
        self.find_element(PromSeacrhLocators.LOGIN_BUTTON).click()
        self.driver.implicitly_wait(200)
        self.find_element(PromSeacrhLocators.EMAIL_BUTTON,time=2).click()
        self.find_element(PromSeacrhLocators.USER_LOGIN_FIELD,time=2).click()
        self.find_element(PromSeacrhLocators.USER_LOGIN_FIELD,time=2).send_keys('gnidetsanna@gmail.com')
        self.find_element(PromSeacrhLocators.DALI_BUTTON,time=2).click()
        self.find_element(PromSeacrhLocators.PASSWORD_FIELD,time=2).click()
        self.find_element(PromSeacrhLocators.PASSWORD_FIELD,time=2).send_keys('Iwanttoworkatpromua1)')
        return self.find_element(PromSeacrhLocators.DALI_2_BUTTON,time=2).click()

    def search_product(self, product_name):
        self.find_element(PromSeacrhLocators.SEARCH_FIELD).clear()
        self.find_element(PromSeacrhLocators.SEARCH_FIELD,time=2).send_keys(product_name)
        return self.find_element(PromSeacrhLocators.SEARCH_BUTTON).click()

    # def parse_product_cart(self):
    #     self.find_element(PromSeacrhLocators.PRODUCT_LINK_1)
    #     if PromSeacrhLocators.PRODUCT_PRODUCER == PromSeacrhLocators.TARGET_PRODUCER_NAME:
    #         self.find_element(PromSeacrhLocators.PRODUCT_LINK).click()
    #     else:
    #         pass
