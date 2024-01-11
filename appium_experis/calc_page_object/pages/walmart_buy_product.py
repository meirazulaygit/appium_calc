from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Walmart_page:

    def __init__(self, driver:webdriver):
        self.driver = driver

    def buy_two_iphons(self):
        go_to_search = self.driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        send_key_to_search = go_to_search.send_keys("iphone 15")

        add_first_iphone = self.driver.find_element(By.XPATH, "//*[@id='maincontent']/main/div/div[2]/div/div/div[1]/div[2]/div/section/div/div[1]/div/div/div/div[1]/div[2]/div[2]/div/button/span")
        add_iphone.click()
        product1_page = self.driver.find_element(By.CSS_SELECTOR, "#maincontent > main > div > div:nth-child(2) > div > div > div.w-100.relative-m.pl4.pr4.flex.pt2 > div.relative.w-80 > div > section > div > div:nth-child(1) > div > div > a")
        go_to_product1_page = product1_page.click()
        price_of_first_iphone = self.driver.find_element(By.CSS_SELECTOR, "#maincontent > section > main > div.flex.undefined.flex-column.h-100 > div:nth-child(2) > div > div.w_aoqv.w_wRee.w_fdPt > div > div:nth-child(2) > div > div > span.b.lh-copy.dark-gray.f1.mr2 > span.inline-flex.flex-column > span")
        price1 = price_of_first_iphone.text[1:]

        add_second_iphone = self.driver.find_element(By.XPATH, "//*[@id='maincontent']/main/div/div[2]/div/div/div[1]/div[2]/div/section/div/div[3]/div/div/div/div[1]/div[2]/div[2]/div/button/span")
        add_second_iphone.click()
        product2_page = self.driver.find_element(By.CSS_SELECTOR, "#maincontent > main > div > div:nth-child(2) > div > div > div.w-100.relative-m.pl4.pr4.flex.pt2 > div.relative.w-80 > div > section > div > div:nth-child(3) > div > div > a")
        go_to_product2_page = product2_page.click()
        price_of_second_iphone = self.driver.find_element(By.CSS_SELECTOR, "#maincontent > section > main > div.flex.undefined.flex-column.h-100 > div:nth-child(2) > div > div.w_aoqv.w_wRee.w_fdPt > div > div:nth-child(2) > div > div > span.b.lh-copy.dark-gray.f1.mr2 > span.inline-flex.flex-column > span")
        price2 = price_of_second_iphone.text[1:]

        price = float(price2 + price1)
        result = str(price)

        price_from_cart_icon = self.driver.find_element(By.CLASS_NAME, "span[class='db nowrap']").text[1:]

        return result, price_from_cart_icon
