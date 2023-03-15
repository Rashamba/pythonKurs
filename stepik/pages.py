from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(url)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    button1 = browser.find_element(By.XPATH, "//button")
    first_window = browser.window_handles[0]
    button1.click()
    time.sleep(4)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(value)
    field = browser.find_element(By.CSS_SELECTOR, "input.form-control")
    field.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button2.click()


finally:
    time.sleep(5)
    browser.quit()
