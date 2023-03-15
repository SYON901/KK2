from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait

from helper_tests import simple_assert, boolean_assert

# Constants
# -----------------------------------------------------------------------------------------------------------------------------------------------
WEBHALLEN_SITE = "https://www.webhallen.com/"

@pytest.fixture
def load_driver():

    # Selenium 4.6 and above use a BETA version of Selenium Manager which automatically handles the browser drivers
    # If we have an older version, or if Selenium Managers somehow does not work on your system, follow this guide for installing the correct driver:
    # https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

    driver = webdriver.Edge()

    # NOT THE BEST SOLUTION BUT USE IT AS A PLACEHOLDER
    # WARNING: THIS DOES NOT WORK WITH EXPLICIT WAIT
    # driver.implicitly_wait(10)

    yield driver

    driver.quit()

# Tests
# -----------------------------------------------------------------------------------------------------------------------------------------------


def test_open_website(load_driver):
    # Load selenium driver
    driver = load_driver
    # Load webhallen website
    driver.get(WEBHALLEN_SITE)

def test_pagetitle (load_driver):
    driver = load_driver
    driver.get(WEBHALLEN_SITE)
    # Test the title of the page
    title = driver.title
    time.sleep(10)
    simple_assert(title, "För gamers och teknikentusiaster - Webhallen.com")


"""     # Finding elements:
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # Actions:
    text_box.send_keys("Selenium")
    submit_button.click()

    # Storing text from an element
    message = driver.find_element(by=By.ID, value="message")
    value = message.text

    # Validate output
    simple_assert(value, "Received!")
 """