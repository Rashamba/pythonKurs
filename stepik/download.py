import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(url)


try:
    first_name = browser.find_element(By.XPATH, "//input[@name='firstname']")
    first_name.send_keys("Test")
    last_name = browser.find_element(By.XPATH, "//input[@name='lastname']")
    last_name.send_keys("Test")
    email = browser.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys("Test")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'resourses/file.txt')           # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)
    button = browser.find_element(By.XPATH, "//button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла