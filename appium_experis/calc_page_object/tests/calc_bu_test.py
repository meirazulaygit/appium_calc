import unittest
from appium import webdriver as a
from appium.webdriver.common.appiumby import AppiumBy
from appium_experis.calc_page_object.pages.calc_page import CalcPage
# from appium_experis.calc_page_object.pages.walmart_buy_product import Walmart_page
from unittest import TestCase
from selenium import webdriver as s
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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
    print("Start test")

    def setUp(self) -> None:
        self.driver_appium = a.Remote(appium_server_url_local, capabilities)
        self.driver_appium.implicitly_wait(10)
        self.calc = CalcPage(self.driver_appium)

        # selenium chrome
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver_chrome = s.Chrome(service=service)

        # Go to AOS URL
        self.driver_chrome.get("https://www.advantageonlineshopping.com/#/")

        self.driver_chrome.maximize_window()

        # When an element is not found, there will be a timeout of 10 seconds
        self.driver_chrome.implicitly_wait(10)

        self.buy_products = Walmart_page(self.driver_chrome)

    def tearDown(self) -> None:
        self.driver_appium.quit()
        self.driver_chrome.quit()

    def test_calc_minus(self):
        self.calc.click_on_number(5)
        self.calc.click_on_minus()
        self.calc.click_on_number(1)
        self.calc.click_on_equals()
        self.assertEqual(self.calc.finel_result(), "4")

    def test_calc_multiplay(self):
        self.calc.click_on_number(4)
        self.calc.click_on_multiplay()
        self.calc.click_on_number(3)
        self.calc.click_on_equals()
        self.assertEqual(self.calc.finel_result(), "12")

    def test_calc_divide(self):
        self.calc.click_on_number(1)
        self.calc.click_on_number(2)
        self.calc.click_on_divide()
        self.calc.click_on_number(3)
        self.calc.click_on_equals()
        self.assertEqual(self.calc.finel_result(), "4")

    def test_calc_plus(self):
        self.calc.click_on_number(4)
        self.calc.click_on_plus()
        self.calc.click_on_number(3)
        self.calc.click_on_equals()
        self.assertEqual(self.calc.finel_result(), "7")
