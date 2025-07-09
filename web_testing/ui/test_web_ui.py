""" from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_google_title():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
 """