import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


expected_result = "Correct!"


@pytest.mark.parametrize('value', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_step1(browser, value):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{value}/step/1"
    browser.get(link)
    button1 = browser.find_element(By.XPATH, "//a[@id='ember33']")
    button1.click()
    field_login = browser.find_element(By.XPATH, "//input[@name='login']")
    field_login.send_keys("rashamba528@gmail.com")
    field_password = browser.find_element(By.XPATH, "//input[@name='password']")
    field_password.send_keys("Jayson999")
    button_authorization = browser.find_element(By.XPATH, "//button[@class='sign-form__btn button_with-loader ']")
    button_authorization.click()
    pop_up = WebDriverWait(browser, 5).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='ember93']")))
    field_text = browser.find_element(By.XPATH, "//div[@class='show-plugin']")
    field_text.send_keys(answer)
    button_send = browser.find_element(By.XPATH, "//button[@class='submit-submission']")
    button_send.click()
    time.sleep(2)
    field_error = browser.find_element(By.XPATH, "//p[@class='smart-hints__hint']").text
    assert field_error == expected_result, f"Expected {expected_result}, got {field_error}"

