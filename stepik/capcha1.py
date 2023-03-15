from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(url)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    field = browser.find_element(By.XPATH, "//input[@class='form-control']")
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


