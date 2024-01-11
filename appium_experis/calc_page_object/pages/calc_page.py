from appium.webdriver.common.appiumby import AppiumBy
import unittest
from appium import webdriver


class CalcPage:
    def __init__(self, driver:webdriver.Remote):
        self.driver = driver

    def click_on_number(self, num:str):
        number = self.driver.find_element(AppiumBy.ID, f"com.google.android.calculator:id/digit_{num}")
        number.click()

    def click_on_multiple(self):
        multiple = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "multiply")
        multiple.click()

    def click_on_divide(self):
        divide = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "divide")
        divide.click()

    def click_on_minus(self):
        minus = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "minus")
        minus.click()

    def click_on_plus(self):
        plus = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "plus")
        plus.click()

    def click_on_equals(self):
        equals = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equals")
        equals.click()

    def finel_result(self):
        final_result = self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final")
        result = final_result.text
        return result

    def preview_result(self):
        preview_result = self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_preview")
        perv_res = preview_result.text
        return perv_res
