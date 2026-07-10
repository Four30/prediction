#from selenium import webdriver

#driver = webdriver.Firefox()

#drivers = driver.get("https://www.cambridgeinternational.org/")
#print(drivers.title)

#from selenium import webdriver

#driver = webdriver.Firefox()

#driver.get("https://www.cambridgeinternational.org/")

#print(driver.title)

#driver.quit()
#running without opening the page
from selenium import webdriver

from selenium.webdriver.firefox.options import Options

options = Options()

options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

driver.get("https://www.google.com")

print("Page title:", driver.title)

driver.quit()