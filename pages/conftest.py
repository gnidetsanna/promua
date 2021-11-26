import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="/home/ahnidets/Desktop/promua/chromedriver")
    #chrome_options = Options()
    #c#hrome_options.add_argument("--disable-extensions")
    #driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()