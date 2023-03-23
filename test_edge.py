from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from helper_tests import simple_assert, boolean_assert

# Constants
# -----------------------------------------------------------------------------------------------------------------------------------------------
WEBHALLEN_SITE = "https://www.webhallen.com/"
class TestClass:
        
    @pytest.fixture(scope="class")
    def load_driver(self):

        driver = webdriver.Edge()

        # NOT THE BEST SOLUTION BUT USE IT AS A PLACEHOLDER
        # WARNING: THIS DOES NOT WORK WITH EXPLICIT WAIT
        driver.implicitly_wait(30)

        yield driver

        driver.quit()
        
    @pytest.fixture
    def get_webhallen_website(self, load_driver):
        driver = load_driver
        driver.get(WEBHALLEN_SITE)
        yield driver
        print("Run test teardown")
        driver.delete_all_cookies()
    # Tests
    # -----------------------------------------------------------------------------------------------------------------------------------------------


    def test_open_url_website(self, get_webhallen_website):
        driver = get_webhallen_website
        boolean_assert("webhallen" in driver.current_url, f"Expected 'webhallen' in url, got: {driver.current_url}")

    def test_page_title (self, get_webhallen_website):
        driver = get_webhallen_website
        title = driver.title
        simple_assert(title, "För gamers och teknikentusiaster - Webhallen.com")

    def test_find_logo(self, get_webhallen_website):
        driver = get_webhallen_website
        #webhallen_logo = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/a"))
        webhallen_logo = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/a")

    def test_click_product1(self, get_webhallen_website):
        driver = get_webhallen_website
        #spel_link = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/div/nav/div/ul/li/a"))
        spel_link = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/nav/div/ul/li/a")
        spel_link.click()
        #ps5_link = WebDriverWait(driver, timeout=30).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/div/nav/div/ul/li/div/ul/li/ul/li/a"))
        ps5_link = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/nav/div/ul/li/div/ul/li/ul/li/a")
        ps5_link.click()
        #ps5_console = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div/div/div/div/div/div/span/span/a"))
        ps5_console = driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div/div/div/div/div/div/span/span/a")
        boolean_assert("Playstation 5 Konsol (PS5)" in ps5_console.text, f"Expected 'Playstation 5 Konsol (PS5)' in text for first product, got: {ps5_console.text}")

    def test_search_valid(self, get_webhallen_website):
        driver = get_webhallen_website
        search_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/div/div/div/input")
        #search_field = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/div/div/div/input"))
        search_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/div/div/div/span/button")
        #search_button = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/div/div/div/span/button"))
        search_field.send_keys("Magic the Gathering: Lord of the Rings Commander Deck Bundle (All 4 decks)")
        search_button.click()
        #progress_text = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div/div/div/div/div/div/span/span/a"))
        progress_text = driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div/div/div/div/div/div/span/span/a")
        boolean_assert("Magic the Gathering: Lord of the Rings Commander Deck Bundle (All 4 decks)" in progress_text.text, f"Expected 'Magic the Gathering: Lord of the Rings Commander Deck Bundle (All 4 decks)' in text for first product, got: {progress_text.text}")
        
    def test_search_invalid(self, get_webhallen_website):
        driver = get_webhallen_website
        search_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/div/div/div/input")
        #search_field = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/div/div/div/input"))
        search_field.send_keys("INVALID_INPUT")
        search_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/div/div/div/span/button")
        #search_button = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/div/div/div/span/button"))
        #search_field.send_keys("INVALID_INPUT")
        search_button.click()
        time.sleep(1)
        #failed_search = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div"))
        failed_search = driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div")
        boolean_assert("Visar 0 av 0 resultat\nVisar 0 av 0 resultat\nFiltrera\nSortera på: Sökrankning" in failed_search.text, f"Expected 'Visar 0 av 0 resultat\nVisar 0 av 0 resultat\nFiltrera\nSortera på: Sökrankning' in text for first product, got: {failed_search.text}")

    def test_last_viewed_product(self, get_webhallen_website):
        driver = get_webhallen_website
        spel_link = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/nav/div/ul/li/a")
        spel_link.click()
        ps5_link = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/nav/div/ul/li/div/ul/li/ul/li/a")
        ps5_link.click()
        #ps5_console = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div/div/div/div/div/div/span/span/a"))
        ps5_console = driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div/div/div/div/div/div/span/span/a")
        ps5_console.click()
        #webhallen_logo = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/a"))
        webhallen_logo = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/a")
        webhallen_logo.click()
        #last_viewed = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/div/div/header/div/div/div/a"))
        last_viewed_menu = driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div/section")
        last_viewed_product = driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div/article/div/div/section/div/div/a")
        boolean_assert(last_viewed_product in last_viewed_menu.text, f"Expected {last_viewed_product} in text for first product, got: {last_viewed_menu.text}")
