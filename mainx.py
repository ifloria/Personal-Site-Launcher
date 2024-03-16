from selenium import webdriver
import chromedriver_autoinstaller
import time


chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

driver.get("https://ifloria.github.io/")
time.sleep(999)