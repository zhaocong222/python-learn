#coding=utf-8
from multiprocessing import Process
import time

def test():
    for i in range(5):
        print("--test--")
        time.sleep(1)

#fork只能在linux下使用(抛弃)，用process解决方案(跨平台)    
p = Process(target=test)
p.start() #让子进程开始执行test函数里的代码，并且执行完函数后进程结束

#主进程继续执行, 这里和fork不一样,主进程并不会立即结束
#这里会一直等待子进程结束后，主进程over
'''
while True:
    print("--main--")
    time.sleep(1)
'''