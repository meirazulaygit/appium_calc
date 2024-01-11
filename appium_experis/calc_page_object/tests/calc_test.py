import unittest
from appium import webdriver as a
from appium.webdriver.common.appiumby import AppiumBy
from appium_experis.calc_page_object.pages.calc_page import CalcPage
from unittest import TestCase
from time import sleep


appium_server_url_local = 'http://localhost:4723/wd/hub'

capabilities = dict(
    platformName='Android',
    deviceName='Pixel7',
    udid="emulator-5554",
    platformVersion="30",
    appActivity='com.android.calculator2.Calculator',
    appPackage='com.google.android.calculator',
    newCommandTimeout=120,
    language='en',
    locale='US'
)


class myFirstTest(unittest.TestCase):
    print ("Start test")

    def setUp(self) -> None:
        self.driver_appium = a.Remote(appium_server_url_local, capabilities)
        self.driver_appium.implicitly_wait(10)
        self.calc = CalcPage(self.driver_appium)

    def tearDown(self) -> None:
        self.driver_appium.quit()

    def test_calc_minus(self):
        self.calc.click_on_number(5)
        self.calc.click_on_minus()
        self.calc.click_on_number(1)
        self.calc.click_on_equals()
        self.assertEqual(self.calc.finel_result(), "4", "the result of minus activity is failed")

    def test_calc_multiple(self):
        self.calc.click_on_number(4)
        self.calc.click_on_multiple()
        self.calc.click_on_number(3)
        self.calc.click_on_equals()
        self.assertEqual(self.calc.finel_result(), "12", "the result of multiple activity is failed")

    def test_calc_divide(self):
        self.calc.click_on_number(1)
        self.calc.click_on_number(2)
        self.calc.click_on_divide()
        self.calc.click_on_number(3)
        self.calc.click_on_equals()
        self.assertEqual(self.calc.finel_result(), "4", "the result of divide activity is failed")

    def test_calc_plus(self):
        self.calc.click_on_number(4)
        self.calc.click_on_plus()
        self.calc.click_on_number(3)
        self.calc.click_on_equals()
        self.assertEqual(self.calc.finel_result(), "7""the result of plus activity is failed")

