import os
import sys
import time
import logging
import unittest

from selenium import webdriver
from datetime import datetime

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Global

webSiteAddress = 'http://192.168.13.213/'
maxWaitTimeSec = 5

class TestCaseKitchenAuthorization(unittest.TestCase):
    
    def setUp(self):#some actions before start test
        self.driver = Global.GetChromeDriver()
        Global.ConfigLogs()

    def tearDown(self):#some actions after test run
        self.driver.close()

    def test_OpenMainPage(self):
        driver = self.driver
        driver.get(webSiteAddress)
        self.assertIn('АИС "Сводный пост"', driver.title, "Не найден заголовок страницы...")

    def test_LoginUser(self):
        driver = self.driver
        driver.get(webSiteAddress)
        login = driver.find_element_by_xpath('//*[@id="username"]')
        password = driver.find_element_by_xpath('//*[@id="password"]')
        btnEnter = driver.find_element_by_xpath('//*[@id="login"]')
        login.send_keys('user_sp')
        password.send_keys('12345')
        btnEnter.click()
        try:
            WebDriverWait(driver, maxWaitTimeSec).until(EC.presence_of_element_located((By.XPATH,'//*[@id="appMenu"]/a[1]')))
            WebDriverWait(driver, maxWaitTimeSec).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[4]/a[1]')))
            WebDriverWait(driver, maxWaitTimeSec).until(EC.visibility_of_element_located((By.CLASS_NAME, 'Logout')))
        except Exception as ex:
            logging.error(ex)
            raise Exception("Login failed. No content.")


        
if __name__ == '__main__':
    unittest.main()