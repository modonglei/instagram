from datetime import time

import requests
from PIL import Image
RecaptchaImagePath = r"D:\CAAutoRegister\img\payload1.jpg"
points = {
    '1': [219,293],
    '2': [349,293],
    '3': [479,293],
    '4': [219,423],
    '5': [349,423],
    '6': [479,423],
    '7': [219,553],
    '8': [349,553],
    '9': [479,553],
}
def getPoint(seq):
    if seq > 3:
        startY = 700
        startX = 0 + 900 * (seq - 4)
    else:
        startY = 0
        startX = 0 + 900 * (seq - 1)
question_dic = {
  "taxis": "/m/0pg52",
  "bus": "/m/01bjv",
  "school bus": "/m/02yvhj",
  "motorcycles": "/m/04_sv",
  "tractors": "/m/013xlm",
  "chimneys": "/m/01jk_4",
  "crosswalks": "/m/014xcs",
  "traffic lights": "/m/015qff",
  "bicycles": "/m/0199g",
  "parking meters": "/m/015qbp",
  "cars": "/m/0k4j",
  "bridges": "/m/015kr",
  "boats": "/m/019jd",
  "palm trees": "/m/0cdl1",
  "mountains or hills": "/m/09d_r",
  "a fire hydrant": "/m/01pns0",
  "stairs": "/m/01lynh"
}

def createTask(question):

    try:
        question = question_dic[question]
    except KeyError as e:
        print(e)
        return False
    url = 'https://api.captcha.run/v2/tasks'
    headers = {
       'Content-Type': 'application/json',
       'Authorization': 'Bearer b3de4dcb-75f3-4dc2-a4ea-8da656825160'
    }
    import base64
    with open(RecaptchaImagePath, "rb") as image_file:
        imageBase64 = base64.b64encode(image_file.read()).decode('utf-8')
    json_data = {
      "captchaType": "ReCaptchaV2Classification",
      'image': imageBase64,
      'question': question,
      'resize': 0,
      "developer": "e277e73d-f6c7-49ea-a920-4e19166c410a"
    }
    response = requests.post('https://api.captcha.run/v2/tasks', headers=headers, json=json_data).json()
    return response


def saveImage():
    import pyautogui
    import time
    pyautogui.moveTo(points['5'][0],points['5'][1])
    pyautogui.rightClick()
    pyautogui.typewrite(['down','v'])
    time.sleep(2)
    pyautogui.typewrite(RecaptchaImagePath)
    pyautogui.typewrite(['Enter'])
