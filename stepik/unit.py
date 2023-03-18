from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_site1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        element1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        element1.send_keys("Test")
        element2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        element2.send_keys("Test")
        element3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        element3.send_keys("Test")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_site2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        element1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        element1.send_keys("Test")
        element2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        element2.send_keys("Test")
        element3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        element3.send_keys("Test")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()

