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

class TestCaseKitchenAuthorization(unittest.TestCase):
    
    def setUp(self):#some actions before start test
        self.driver = Global.GetChromeDriver()

    def tearDown(self):#some actions after test run
        self.driver.close()

    def test_OpenMainPage(self):
        driver = self.driver
        driver.get('http://kitchen/')
        assert 'Они обедают в офисе - Запишись на обед' in driver.title  
        
    def test_LoginFormOpen(self):
        self.assertEqual(1, 1, "Is not equal!") 
        
if __name__ == '__main__':
    unittest.main()