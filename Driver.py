import time

from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import pyautogui
# id = '4f263436b1854b16a5ab53b65cc03a73'
# res = openBrowser(id)
# driverPath = res['data']['driver']
# debuggerAddress = res['data']['http']
# print(driverPath)
# print(debuggerAddress)
# selenium 连接代码
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", '127.0.0.1:50095')
chrome_service = Service(r'C:\Users\莫冬雷\AppData\Roaming\BitBrowser\chromedriver\118\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.set_page_load_timeout(60)
# driver.close()
# time.sleep(3)
# driver.find_element(By.XPATH,'//span[text() = "搜索"]').click()
# time.sleep(2)
# WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="搜索"]'))).send_keys('777_zone4')
# time.sleep(1)
# WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//div/span[text() = "777_zone4"]'))).click()
# time.sleep(1)
# WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//a[text() = "粉丝"]'))).click()
# time.sleep(1)
#
# 模拟滚动操作
# fsElm = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//div[@class = "_aano"]')))
# while True:
#     # 滚动到懒加载元素底部
#
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", fsElm)
#     time.sleep(4)
#     # 判断页面是否已经滚动到底部
#     last_height = driver.execute_script("return arguments[0].scrollHeight", fsElm)
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", fsElm)
#     time.sleep(4)
#     new_height = driver.execute_script("return arguments[0].scrollHeight", fsElm)
#     if new_height == last_height:
#         break

# 找到需要悬停的元素
elements = driver.find_elements(By.XPATH,'//div[@class = "_aano"]//div[@tabindex="0"]')
driver.execute_script("arguments[0].scrollIntoView();", elements[0])
time.sleep(1)
# 创建 ActionChains 对象
actions = ActionChains(driver)

# 将鼠标悬停在元素上
actions.move_to_element(elements[0]).perform()
time.sleep(1)
print(driver.find_element(By.XPATH, '//span[text() = "粉丝"]/../../div[1]/span').text)











