from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    # options.add_argument("--headless")  # ❗ If you want to see the browser, comment this out
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver

BASE_URL = "http://localhost:59104"

