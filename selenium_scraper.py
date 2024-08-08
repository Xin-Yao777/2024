from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
time.sleep(5)

elem = driver.find_element(By.NAME, "q")
time.sleep(5)

elem.clear()
elem.send_keys("pycon")
time.sleep(5)

elem.send_keys(Keys.RETURN)
time.sleep(20)
assert "No results found." not in driver.page_source
driver.close()

print("Done")