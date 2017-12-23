import os
import time

#创建了一个子进程， 子进程也从这开始执行
#父进程 ret>0 ,子进程ret =0
ret = os.fork()

#父进程先结束
#5秒后子进程结束

if ret == 0:
    print("---子进程---")
    time.sleep(5)
    print("---子进程over---")
else:
    print("---父进程---")
    time.sleep(3)
