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
# res = groupList()
# id = browserList(res['data']['list'][1]['id'])['data']['list'][0]['id']
# res = openBrowser(id)
# driverPath = res['data']['driver']
# debuggerAddress = res['data']['http']
# print(driverPath)
# print(debuggerAddress)
# # selenium 连接代码
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", '127.0.0.1:56866')
chrome_service = Service(r'C:\Users\莫冬雷\AppData\Roaming\BitBrowser\chromedriver\118\chromedriver.exe')

# chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)
# chrome_service = Service(driverPath)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.set_page_load_timeout(60)
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(5)
# try:
#     driver.find_element(By.XPATH,'//*[text() = "以后再说"]').click()
# except Exception as e:
#     print(e)
# WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//span[text() = "搜索"]'))).click()
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
# def checkUpdate():
#     elm_lenth = len(driver.find_elements(By.XPATH, '//div[@class = "_aano"]//div[@tabindex="0"]'))
#     for i in range(10):
#         elements = driver.find_elements(By.XPATH, '//div[@class = "_aano"]//div[@tabindex="0"]')
#         if len(elements) > elm_lenth:
#             time.sleep(2)
#             elm_lenth = len(driver.find_elements(By.XPATH, '//div[@class = "_aano"]//div[@tabindex="0"]'))
#             break
#         time.sleep(1)
#
# while True:
#     # 滚动到懒加载元素底部
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", fsElm)
#     checkUpdate()
#     # 判断页面是否已经滚动到底部
#     last_height = driver.execute_script("return arguments[0].scrollHeight", fsElm)
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", fsElm)
#     checkUpdate()
#     new_height = driver.execute_script("return arguments[0].scrollHeight", fsElm)
#     if new_height == last_height:
#         break

# 找到需要悬停的元素
# elements = driver.find_elements(By.XPATH,'//div[@class = "_aano"]//div[@tabindex="0"]')
# for i in range(len(elements)):
#     driver.execute_script("arguments[0].scrollIntoView();", elements[i])
#     time.sleep(1)
#     # 创建 ActionChains 对象
#     actions = ActionChains(driver)
#     # 将鼠标悬停在元素上
#     actions.move_to_element(elements[i]).perform()
#     time.sleep(1)
#     fs_lenth = int(driver.find_element(By.XPATH, '//span[text() = "粉丝"]/../../div[1]/span').text)
#     if fs_lenth >= 1000:
#         nameElms = driver.find_elements(By.XPATH,'//div[@class = "_aano"]//div[@tabindex="0"]/../../../../..//span[@class = "_ap3a _aaco _aacw _aacx _aad7 _aade"]')
#         actions = ActionChains(driver)
#         actions.key_down(Keys.CONTROL).click(nameElms[i]).key_up(Keys.CONTROL).perform()
#         time.sleep(1)
#         # 切换到最新标签页
#         driver.switch_to.window(driver.window_handles[-1])
#         time.sleep(1)
#         print(driver.title)
#         driver.close()
#         time.sleep(1)
#         driver.switch_to.window(driver.window_handles[0])
#         time.sleep(1)
#
#     else:
#         driver.find_element(By.XPATH,'//div[text() = "粉丝"]').click()

# WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@class="_aarf _aarg"]'))).click()

WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@placeholder,"回复")]'))).send_keys('hellow')
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[text()="Direct"]/..'))).click()










