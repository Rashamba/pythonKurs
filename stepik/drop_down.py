from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

url = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(url)

try:
    num1 = (browser.find_element(By.CSS_SELECTOR, "#num1")).text
    num2 = (browser.find_element(By.CSS_SELECTOR, "#num2")).text
    sum = int(num1) + int(num2)

    dropdown = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    dropdown.select_by_value(str(sum))
    button = browser.find_element(By.XPATH, "//button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
