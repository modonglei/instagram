import multiprocessing
import time
import test
from logTool import log

def runAutoTask():
    try:
        test.taskRun()
    except Exception as e:
        log.info(e)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    pool = multiprocessing.Pool(processes=6)
    for i in range(1):
        handler = pool.apply_async(runAutoTask)
        # time.sleep(5)
    pool.close()
    pool.join()



