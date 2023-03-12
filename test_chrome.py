from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
# import time
from selenium.webdriver.support.wait import WebDriverWait

from helper_tests import simple_assert, boolean_assert

# Constants
# -----------------------------------------------------------------------------------------------------------------------------------------------
SELENIUM_SITE = "https://www.selenium.dev/selenium/web/web-form.html"
ICEBERRY_SITE = "https://scar.sandbox.iceberry.se/"

# Fixtures and helpers
# -----------------------------------------------------------------------------------------------------------------------------------------------


# Helper for waiting explicitly
# def document_initialised(driver):
#     return driver.execute_script("return initialised")


# Setup and Teardown for each selenium test
@pytest.fixture
def load_driver():

    # Selenium 4.6 and above use a BETA version of Selenium Manager which automatically handles the browser drivers
    # If we have an older version, or if Selenium Managers somehow does not work on your system, follow this guide for installing the correct driver:
    # https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

    driver = webdriver.Chrome()

    # NOT THE BEST SOLUTION BUT USE IT AS A PLACEHOLDER
    # WARNING: THIS DOES NOT WORK WITH EXPLICIT WAIT
    # driver.implicitly_wait(5)

    yield driver

    driver.quit()


# Tests
# -----------------------------------------------------------------------------------------------------------------------------------------------


def test_1(load_driver):

    driver = load_driver

    driver.get(SELENIUM_SITE)

    # Test the title of the page
    title = driver.title
    simple_assert(title, "Web form")

    # Finding elements:
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

    
# Test an exception
def test_2(load_driver):

    driver = load_driver

    driver.get(SELENIUM_SITE)

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # Missing method
    with pytest.raises(AttributeError):
        submit_button.faulty_click()


def test_lecture_1(load_driver):
    # Load Selenium webdriver
    driver = load_driver

    # Load iceberry website
    driver.get(ICEBERRY_SITE)

    # Test that iceberry is part of the url
    boolean_assert("iceberry" in driver.current_url, f"Expected iceberry in url, got: {driver.current_url}")

    # Find the header element on the site by XPATH
    heading = driver.find_element(By.XPATH, "/html/body/div/main/header/div/h1")

    # Test that the header contains the corect text
    # boolean_assert("SCAR ENERGY" in heading.text, f"Expected SCAR ENERGY in url, got: {heading.text}")
    simple_assert(heading.text, "SCAR ENERGY DRINK")

    # Find products page link
    products_link = driver.find_element(By.LINK_TEXT, "Products")

    # Click on products page link
    products_link.click()

    # BAD SOLUTION. Show anyway
    # time.sleep(1)
    
    # Find original Scar text (Without explicit waiting)
    # scar_original = driver.find_element(By.XPATH, "/html/body/div/main/section/div/main/a[1]/div/div[2]/h2")

    # Including explicit wait
    # WARNING: This does not work together with implicit wait
    scar_original = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/main/section/div/main/a[1]/div/div[2]/h2"))

    # Test that the text contains "Scar Original"
    boolean_assert("Scar Original" in scar_original.text, f"Expected Scar Original in text for first product, got: {scar_original.text}")

    # Test that url now contains products
    boolean_assert("products" in driver.current_url, f"Expected products in url, got: {driver.current_url}")