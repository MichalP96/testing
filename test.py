from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Users\xxpekmic\Desktop\TestQA\Driver\chromedriver.exe")
driver.get("https://www.python.org")
time.sleep(10)
assert driver.title == "Welcome to Python.org"
driver.quit()