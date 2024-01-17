import datetime
import logging
import multiprocessing
import os
process_name = multiprocessing.current_process().name
file_path = rf'D:\AutoRegist\log\{datetime.date.today()}{process_name}.txt'
file_path2 = rf'D:\AutoRegist\log\{datetime.date.today()}.txt'
def creat(file_path):
    # 判断文件所在的目录是否存在，如果不存在则创建
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 判断文件是否存在，如果不存在则创建
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass
def configLog():
    # 设置日志的基本配置
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    # 创建一个FileHandler，指定日志文件的路径和模式
    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(logging.INFO)
    file_handler2 = logging.FileHandler(file_path2)
    file_handler2.setLevel(logging.INFO)
    # 创建一个Formatter，指定日志的格式
    formatter = logging.Formatter(f'%(asctime)s - %(levelname)s - %(message)s')
    formatter2 = logging.Formatter(f'{process_name} - %(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    file_handler2.setFormatter(formatter2)
    # 将FileHandler添加到logger
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.addHandler(file_handler2)
    return logger

creat(file_path)
creat(file_path2)
log = configLog()

