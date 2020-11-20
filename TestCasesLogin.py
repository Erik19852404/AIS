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

loginPass = {
    'correctLogin' : 'user_sp',
    'correctPassword' : '12345',
    'emptyLogin' : '',
    'emptyPassword' : ''
}

class TestCaseAuthorization(unittest.TestCase):    
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
        self.Login(loginPass['correctLogin'], loginPass['correctPassword'])
        WebDriverWait(driver, maxWaitTimeSec).until(EC.presence_of_element_located((By.XPATH,'//*[@id="appMenu"]/a[1]')))
        WebDriverWait(driver, maxWaitTimeSec).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[4]/a[1]')))
        WebDriverWait(driver, maxWaitTimeSec).until(EC.visibility_of_element_located((By.CLASS_NAME, 'Logout')))

    def test_LoginEmpty(self):
        driver = self.driver
        driver.get(webSiteAddress)
        self.Login(loginPass['emptyLogin'], loginPass['emptyPassword'])
        WebDriverWait(driver, maxWaitTimeSec).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]'))


    def Login(self, userLogin, userPassword):
        driver = self.driver
        login = driver.find_element_by_xpath('//*[@id="username"]')
        password = driver.find_element_by_xpath('//*[@id="password"]')
        btnEnter = driver.find_element_by_xpath('//*[@id="login"]')
        login.send_keys(userLogin)
        password.send_keys(userPassword)
        btnEnter.click()
        
if __name__ == '__main__':
    unittest.main()