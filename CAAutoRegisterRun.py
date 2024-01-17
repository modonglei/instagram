import multiprocessing
from logTool import log
import bit_selenium
import pandas as pd
def getDataFrame(filePath):
    dataFrame = pd.read_excel(filePath)
    l = len(dataFrame)
    log.info(f'本次运行的数据为：\n{dataFrame.to_string()}')
    log.info(f'本次数据的量为{l}条')
    return dataFrame


def AutoTask(lock,index, RegisterData,host, port, proxyUserName, proxyPassword,tlUsname,tlPwd,col):
    # 共享变量的data类型为<class 'multiprocessing.managers.ListProxy'>，虽然可以取到第二层数据但无法修改，只能修改第一层数据，所以还是想转换再重新赋值
    listData = RegisterData[index]
    listData = bit_selenium.BrowserRun(lock,listData,host, port, proxyUserName, proxyPassword,tlUsname,tlPwd,col)
    RegisterData[index] = listData
    log.info(RegisterData[index])


if __name__ == '__main__':
    multiprocessing.freeze_support()
    lock = multiprocessing.Lock()
    try:
        filePath = rf'D:\AutoRegist\Register.xlsx'
        configFilePath = rf'D:\AutoRegist\config.xlsx'
        df = getDataFrame(filePath)
        config_df = getDataFrame(configFilePath)
        processes_lenth = config_df['多开窗口数量'][0]
        tlUsname = config_df['图灵打码账号'][0]
        tlPwd = config_df['图灵打码密码'][0]
        host = config_df['代理主机'][0]
        port = config_df['代理端口'][0]
        proxyUserName = config_df['代理账号'][0]
        proxyPassword = config_df['代理密码'][0]
        col = config_df['每行列数'][0]
        processes_lenth = processes_lenth
        dataList = df.values.tolist()
        manager = multiprocessing.Manager()
        data = manager.list(dataList)
        pool = multiprocessing.Pool(processes=processes_lenth)
        # 将每个数据分配给一个进程进行处理
        for i, item in enumerate(data):
            pool.apply_async(AutoTask, args=(lock,i, data,host, port, proxyUserName, proxyPassword,tlUsname,tlPwd,col))
        # 关闭结束进程
        pool.close()
        pool.join()
        header_list = df.columns.tolist()
        data.insert(0, header_list)
        df = pd.DataFrame(data[1:], columns=data[0])
        df.to_excel(filePath, index=False, sheet_name='Sheet1', engine='openpyxl')
    except Exception as e:
        log.info(e)





