from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(url)

    chest = browser.find_element(By.CSS_SELECTOR, "#treasure")
    value = chest.get_attribute("valuex")
    y = calc(value)

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