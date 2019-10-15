from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = None

def setup_function(function):
    global browser
    browser = webdriver.Chrome()
    browser.get("http://www.python.org")
    assert "Python" in browser.title

def teardown_function(self):
    global browser
    if browser:
        browser.close()
    browser = None

def test_no_results():
    search_box = browser.find_element_by_name("q")
    search_box.clear()
    search_box.send_keys("sjdkfnsdfjnsd")
    search_box.send_keys(Keys.RETURN)
    assert "No results found." in browser.page_source        

def test_result_is_found():
    search_box = browser.find_element_by_name("q")
    search_box.clear()
    search_box.send_keys("pycon")
    search_box.send_keys(Keys.RETURN)
    assert "No results found." not in browser.page_source        
