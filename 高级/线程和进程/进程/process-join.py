from multiprocessing import Process
import time

def test():
    while True:
        print("--test--")
        time.sleep(1)
    
p = Process(target=test)
p.start() #让这个进程开始执行test函数里的代码

#阻塞，等进程p(子进程)结束后，主进程继续往后执行
p.join()
#p.join(1) #等待1秒

print("------xxx------")