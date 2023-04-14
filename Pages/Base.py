from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECO


class Base:

    def __init__(self, driver):
        self.driver = driver

    def clickToElement(self, element):
        WebDriverWait(self.driver, 10).until(ECO.visibility_of_element_located(element)).click()

    def sendTextToElement(self, element, text):
        WebDriverWait(self.driver, 10).until(ECO.visibility_of_element_located(element)).send_keys(text)

    def visibilityOfElement(self, element):
        el = WebDriverWait(self.driver, 10).until(ECO.visibility_of_element_located(element))
        return bool(el)
