from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
# import time
from selenium.webdriver.support.wait import WebDriverWait

from helper_tests import simple_assert, boolean_assert

# Constants
# -----------------------------------------------------------------------------------------------------------------------------------------------
WEBHALLEN_SITE = "https://www.webhallen.com/"

@pytest.fixture
def load_driver():

    driver = webdriver.Edge()

    # NOT THE BEST SOLUTION BUT USE IT AS A PLACEHOLDER
    # WARNING: THIS DOES NOT WORK WITH EXPLICIT WAIT
    # driver.implicitly_wait(10)

    yield driver

    driver.quit()

# Tests
# -----------------------------------------------------------------------------------------------------------------------------------------------


def test_open_url_website(load_driver):
    # Load selenium driver
    driver = load_driver
    # Load webhallen website
    driver.get(WEBHALLEN_SITE)
    boolean_assert("webhallen" in driver.current_url, f"Expected 'webhallen' in url, got: {driver.current_url}")

def test_page_title (load_driver):
    driver = load_driver
    driver.get(WEBHALLEN_SITE)
    # Test the title of the page
    title = driver.title
    simple_assert(title, "För gamers och teknikentusiaster - Webhallen.com")

def test_find_logo(load_driver):
    driver = load_driver
    driver.get(WEBHALLEN_SITE)
    webhallen_logo = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/a/div/div")

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