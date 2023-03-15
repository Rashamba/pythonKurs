import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(url)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    value = (browser.find_element(By.CSS_SELECTOR, "#input_value")).text
    y = calc(value)
    browser.execute_script("window.scrollBy(0, 100);")
    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(y)
    box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    box.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    button = browser.find_element(By.XPATH, "//button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла