from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    element1.send_keys("Test")
    element2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    element2.send_keys("Test")
    element3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    element3.send_keys("Test")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

    