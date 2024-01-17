import base64
import multiprocessing
import random
import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from bit_api import *
from selenium.webdriver.common.action_chains import ActionChains
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", '127.0.0.1:54388')

# '''127.0.0.1:54388   127.0.0.1:54407'''
# chrome_service = Service(r'C:\\Users\\莫冬雷\\AppData\\Roaming\\BitBrowser\\chromedriver\\112\\chromedriver.exe')
# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
def 图灵打码(username, password, b64, ID):
    data = {"username": username, "password": password, "ID": ID, "b64": b64, "version": "3.1.1"}
    data_json = json.dumps(data)
    result = json.loads(requests.post("http://www.fdyscloud.com.cn/tuling/predict", data=data_json).text)
    return result

def 生成滑动轨迹(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 3
    while current < distance:
        if current < mid:
            # 加速度为正2
            a = random.randint(1, 3)
        else:
            # 加速度为负3
            a = random.randint(-3, -2)
        # 初速度v0
        v0 = v
        # 当前速度v = v0 + at
        v = v0 + a * t
        # 移动距离x = v0t + 1/2 * a * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += round(move)
        # 加入轨迹
        track.append(round(move))
    print(sum(track))
    return track
def dropHK(driver,tlUsname,tlPwd):
    # iframe = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//iframe[@scrolling="yes"]')))
    iframe = driver.find_element(By.XPATH,'//iframe[@scrolling="yes"]')
    driver.switch_to.frame(iframe)
    time.sleep(1)
    验证码 = driver.find_element(By.XPATH,'//*[@id="captcha__puzzle"]/canvas[@class = "block"]').screenshot_as_base64
    # 将base64编码解码为字节数据
    from PIL import Image
    from io import BytesIO
    image_data = base64.b64decode(验证码)
    # 将字节数据转换为Image对象
    image = Image.open(BytesIO(image_data))
    # 保存图片到本地
    process_name = multiprocessing.current_process().name
    image.save(rf'D:\AutoRegist\{process_name}image.png')
    res = 图灵打码(tlUsname,tlPwd,验证码,"48956156")
    print(res)
    x = int(res['data']['缺口']['X坐标值'] - 19)
    print(x)

    滑动轨迹=生成滑动轨迹(x)
    # print(滑动轨迹)
    滑块=driver.find_element(By.XPATH,'//*[@class="slider"]')
    ActionChains(driver).click_and_hold(滑块).pause(0.2).perform()
    for x in 滑动轨迹:
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=random.randint(-2, 2)).perform()
        # time.sleep(random.uniform(0.1, 0.2))
    ActionChains(driver).pause(0.2).release().perform()



# hk = driver.find_element(By.XPATH,'//*[@class="slider"]')
# action = ActionChains(driver)
# # 鼠标操作对象
# action.click_and_hold(hk)
# action.pause(0.2)
# # 鼠标偏移
# action.move_by_offset(x, 0)
# # 特殊清空，鼠标便宜不够手动添加
# action.pause(0.6)
# # 松开鼠标
# action.release()
# # 执行action内设置的操作
# action.perform()



