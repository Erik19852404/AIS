import os
import time
import logging
import unittest
import threading

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pathLog = 'D:\\AIS\\AutoTests\\AIS\Logs\\LogDebug.txt'
pathChromeDriver = r'D:\\AIS\\AutoTests\\AIS\\Drivers\\chromedriver.exe'
driver = None
threadLock = threading.Lock()
exitFlag = 0

def RemoveOldLogs(logPaths):
    for logPath in logPaths:
        if os.path.exists(logPath):
            os.remove(logPath)

def SetPathLogs(_path):
    logging.basicConfig(filename=_path, encoding='utf-8', level=logging.DEBUG)

def ConfigLogs():
    SetPathLogs(pathLog[0:len(pathLog) - 4] + datetime.now().strftime("%d_%m_%H_%M_%S") + pathLog[len(pathLog) - 4:])

def GetChromeDriver():
    return webdriver.Chrome(executable_path=pathChromeDriver)

def GetFirefoxDriver():
    return webdriver.Firefox()

class GetNewThread (threading.Thread):
    def __init__(self, name, counter, func, args):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
        self.func = func
        self.args = args
    def run(self):
        print("\nStarting " + self.name)
        # Acquire lock to synchronize thread
        threadLock.acquire()
        try:
            if isinstance(self.args, list):
                self.func(self, *self.args[1:])
            else:
                self.func()
        except Exception as ex:
            print(ex)
            logging.error(ex)
        # Release lock for the next thread
        threadLock.release()
        print("Exiting " + self.name)
# Create new thread
#thread1 = myThread("Thread", 1, myFunc(), None)
# Start new Thread
#thread1.start()
# Wait for all thread to complete
#thread1.join()