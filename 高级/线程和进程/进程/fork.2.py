import os
import time

#创建了一个子进程， 子进程也从这开始执行
#父进程 ret>0 ,子进程ret =0
ret = os.fork()

if ret > 0:
    print("---父进程---%d"%os.getpid())
else:
    print("---子进程---%d"%os.getpid())
    print("---父进程---%d"%os.getppid())

