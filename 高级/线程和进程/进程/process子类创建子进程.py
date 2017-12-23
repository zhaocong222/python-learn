from multiprocessing import Process
import time

#继承Process
class MyProcess(Process):
    #需要定义run方法
    def run(self):
        while True:
            print("--1--")
            time.sleep(1)
        
p = MyProcess()
#开启子进程，程序会自动调用 run方法
p.start()

while True:
    print("---main---")
    time.sleep(1)