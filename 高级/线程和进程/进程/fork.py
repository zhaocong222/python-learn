import os
import time

#创建了一个子进程， 子进程也从这开始执行
#父进程 ret>0 ,子进程ret =0
ret = os.fork()

if ret == 0:
    while True:
        print("------1----")
        time.sleep(1)
else:
    while True:
        print("------2-----")
        time.sleep(1)