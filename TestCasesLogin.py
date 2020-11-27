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
ByParamsForGetElement = {
    'byXPath' : 'find_element_by_xpath',
    'byCSS' : "find_element_by_css_selector",
    'byClass' : 'find_element_by_class_name',
    'byID' : 'find_element_by_id',
    'byName' : 'find_element_by_name',
    'byText' : 'find_element_by_partial_link_text',
    'byTag' : 'find_element_by_tag_name'
}
loginPass = {
    'correctLogin' : 'user_sp',
    'emptyLogin' : '',
    'wrongUserLogin' : 'user_wrong',
    'correctPassword' : '12345',
    'emptyPassword' : ''
}
testResult = {
    "Unknown" : "Test was not run...",
    "Success" : "Test was complete successfully...",
    "Failed" : "Test failed..."
}

class TestCaseAuthorization(unittest.TestCase):    
    def setUp(self):#some actions before start test
        self.driver = Global.GetChromeDriver()
        Global.ConfigLogs()

    def tearDown(self):#some actions after test run
        self.driver.close()

    def doModuleCleanups():#called unconditionally after test
        pass

    def test_OpenMainPage(self):
        driver = self.driver
        driver.get(webSiteAddress)
        self.assertIn('АИС "Сводный пост"', driver.title, "Не найден заголовок страницы...")

    def test_LoginUser(self):
        driver = self.driver
        driver.get(webSiteAddress)
        self.assertEqual(self.Login(loginPass['correctLogin'], loginPass['correctPassword']), testResult['Success'], 'Login')
        self.CheckElementPresence(By.XPATH,'//*[@id="appMenu"]/a[1]', "Menu")
        self.CheckElementPresence(By.XPATH,'//*[@id="content"]/div[4]/a[1]', "Content container")
        self.CheckElementPresence(By.CLASS_NAME, 'Logout', "Logout button")

    def test_LoginEmpty(self):
        driver = self.driver
        driver.get(webSiteAddress)
        self.Login(loginPass['emptyLogin'], loginPass['emptyPassword'])
        self.CheckElementPresence(By.XPATH, '/html/body/div[3]', "Wrong login message window")

    def test_LoginWrongUser(self):
        driver = self.driver
        driver.get(webSiteAddress)
        self.Login(loginPass['wrongUserLogin'], loginPass['emptyPassword'])
        self.CheckElementPresence(By.XPATH, '/html/body/div[3]', "Wrong login message window")

    def Login(self, userLogin, userPassword):
        result = testResult['Unknown']
        login = self.GetElement('byXPath', '//*[@id="username2"]', 'Login field')
        password = self.GetElement('byXPath', '//*[@id="password"]', 'Password field')
        btnEnter = self.GetElement('byXPath', '//*[@id="login"]', 'Confirm button')
        if login != None and password != None and btnEnter != None:
            login.send_keys(userLogin)
            password.send_keys(userPassword)
            btnEnter.click()
            result = testResult['Success']
        else:
            result = testResult['Failed']
        return result

    def CheckElementPresence(self, ByParams, elementIdentificator, elementName):
        driver = self.driver
        try:
            WebDriverWait(driver, maxWaitTimeSec).until(EC.presence_of_element_located((ByParams, elementIdentificator)))
        except Exception as ex:
            print("No presence of element '" + elementName + "'...")
            logging.error(ex)

    def GetElement(self, ByParamsStr, elementIdentificator, elementName):
        driver = self.driver
        element = None
        try:
            getElementFunc = getattr(driver, ByParamsForGetElement[ByParamsStr])
            element = getElementFunc(elementIdentificator) 
        except Exception as ex:
            print("Can't get element '" + elementName + "'...")
            logging.error(ex)
        return element

        
if __name__ == '__main__':
    unittest.main()