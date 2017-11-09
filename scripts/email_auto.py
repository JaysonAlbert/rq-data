from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://passport.yandex.com/registration/")

driver.find_element_by_class_name("human-confirmation-switch-wrap").click()
for i in range(1000):
    element = driver.find_element_by_class_name("pseudo_link")
    element.click()
    element = driver.find_element_by_class_name("captcha__captcha__text")
    url  = element.get_attribute("src")
    urllib.urlretrieve(url,"images/" + url[-10:] + ".png")
    time.sleep(0.5)

# element = driver.find_element_by_xpath('//iframe[@title="recaptcha widget"]')
# driver.switch_to_frame(element)
# element = driver.find_element_by_id('recaptcha-anchor')
# element.click()
# time.sleep(3)
