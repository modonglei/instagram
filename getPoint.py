from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from bit_api import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# f.proxys5.net:6200:35343298-zone-custom-region-CA:iOOB7eKW
# browser_id = createBrowser('f.proxys5.net', '6200', '35343298-zone-custom-region-CA', 'iOOB7eKW')
# res = openBrowser(browser_id)
# driverPath = res['data']['driver']
# debuggerAddress = res['data']['http']
# print(driverPath)
# print(debuggerAddress)

# selenium 连接代码
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", '127.0.0.1:50172')
chrome_service = Service(r'C:\Users\莫冬雷\AppData\Roaming\BitBrowser\chromedriver\112\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe')))
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="ctp-checkbox-label"]'))).screenshot('img/bb.jpg')

import pyautogui
time.sleep(4)
# loc = pyautogui.locateCenterOnScreen("img/bb.jpg") # region参数限制查找范围，加快查找速度
# loc = pyautogui.locateCenterOnScreen("img/aa.jpg") # region参数限制查找范围，加快查找速度
# print(loc)
# pyautogui.moveTo(*loc, duration=0.5) # 移动鼠标
# pyautogui.click(clicks=1) #点击


