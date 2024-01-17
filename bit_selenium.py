from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dropHK


def typeCheck(data):
    if data != str:
        data = str(data)
    return data
def RunRegister(listData,browser_id,tlUsname,tlPwd,col):
    # /browser/open 接口会返回 selenium使用的http地址，以及webdriver的path，直接使用即可
    res = openBrowser(browser_id)
    col = int(col)
    windowbounds(col)
    driverPath = res['data']['driver']
    debuggerAddress = res['data']['http']
    print(driverPath)
    print(debuggerAddress)
    # selenium 连接代码
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)
    chrome_service = Service(driverPath)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.set_page_load_timeout(60)
    driver.get('https://canadiandiamondsclassaction.ca/en/claim/consumer')
    time.sleep(15)
    try:
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="virtualCode"]'))).send_keys(listData[0])
    except:
        driver.refresh()
        time.sleep(12)
        # tlUsname图灵打码用户名, tlPwd图灵打码密码
        dropHK.dropHK(driver,tlUsname,tlPwd)
        time.sleep(10)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="virtualCode"]'))).send_keys(listData[0])
    time.sleep(3)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="enterCodeButtonLabelWrapper"]'))).click()
    try:
        WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="addFirstName"]'))).send_keys(listData[1])
    except:
        driver.refresh()
        time.sleep(13)
        # tlUsname图灵打码用户名, tlPwd图灵打码密码
        dropHK.dropHK(driver,tlUsname,tlPwd)
        time.sleep(10)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="addFirstName"]'))).send_keys(listData[1])
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="addLastName"]'))).send_keys(listData[2])
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="addLine1"]'))).send_keys(listData[3])
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="addCity"]'))).send_keys(listData[4])
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="addZIPCode"]'))).send_keys(typeCheck(listData[6]))
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="addPhoneNumber"]'))).send_keys(typeCheck(listData[7]))
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="emailAddressBilling"]'))).send_keys(listData[8])
    time.sleep(2)
    StateElement = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="addRegion"]')))
    select = Select(StateElement)
    select.select_by_value(listData[5])
    time.sleep(2)
    driver.execute_script('window.scrollBy(0,280)')
    time.sleep(2)
    driver.find_elements(By.XPATH,'//*[@class="checkmark fa"]')[0].click()
    time.sleep(2)
    driver.find_elements(By.XPATH,'//*[@class="checkmark fa"]')[1].click()
    time.sleep(2)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="addressRegisterText"]'))).click()
    time.sleep(1)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[text() = " Use Entered Address "]'))).click()
    time.sleep(14)
    try:
        RegisterResultText = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//app-card-layout'))).text
        for j in range(10):
            if '...' in RegisterResultText:
                print(RegisterResultText)
                time.sleep(2)
                RegisterResultText = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//app-card-layout'))).text
            else:
                break
    except:
        driver.refresh()
        time.sleep(13)
        # tlUsname图灵打码用户名, tlPwd图灵打码密码
        dropHK.dropHK(driver,tlUsname,tlPwd)
        time.sleep(10)
        RegisterResultText = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//app-card-layout'))).text
        for j in range(10):
            if '...' in RegisterResultText:
                print(RegisterResultText)
                time.sleep(2)
                RegisterResultText = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//app-card-layout'))).text
            else:
                break
    lines = RegisterResultText.split('\n')  # 将文本按行拆分成列表
    new_text = '\n'.join(lines[:-1])  # 取除了最后一行以外的所有行，并重新连接起来
    listData[9] = new_text
    listData[10] = '成功'



def BrowserRun(lock,listData,host, port, proxyUserName, proxyPassword,tlUsname,tlPwd,col):
    log.info(listData)
    port = typeCheck(port)
    for i in range(8):
        browser_id = createBrowser(host, port, proxyUserName, proxyPassword)
        try:
            RunRegister(listData,browser_id,tlUsname,tlPwd,col)
        except Exception as e:
            log.info(e)
            listData[10] = '失败'
        time.sleep(1)
        closeBrowser(browser_id)
        time.sleep(5)
        deleteBrowser(browser_id)
        if listData[10] == '成功':
            break
    return listData

def StaticIPBrowserRun(listData,dynamicIpUrl,dynamicIpChannel,tlUsname,tlPwd,col):
    log.info(listData)
    for i in range(8):
        browser_id = createStaticBrowser(dynamicIpUrl,dynamicIpChannel)
        try:
            RunRegister(listData,browser_id,tlUsname,tlPwd,col)
        except Exception as e:
            log.info(e)
            listData[10] = '失败'
        time.sleep(1)
        closeBrowser(browser_id)
        time.sleep(5)
        deleteBrowser(browser_id)
        if listData[10] == '成功':
            break
    return listData