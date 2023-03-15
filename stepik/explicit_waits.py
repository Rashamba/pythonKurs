from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

url = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(url)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    button1 = browser.find_element(By.CSS_SELECTOR, "#book")
    button1.click()
    browser.execute_script("window.scrollBy(0, 100);")
    value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(value)
    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    button2.click()


finally:
    time.sleep(10)
    browser.quit()

