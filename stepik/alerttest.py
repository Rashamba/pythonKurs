from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(url)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    button1 = browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    value = (browser.find_element(By.CSS_SELECTOR, "#input_value")).text
    y = calc(value)
    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(y)
    button2 = browser.find_element(By.XPATH, "//button")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()




