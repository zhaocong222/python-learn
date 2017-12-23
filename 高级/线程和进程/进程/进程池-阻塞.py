from multiprocessing import Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    #random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2) 
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))

po=Pool(3) #定义一个进程池，最大进程数3
for i in range(0,10):
    po.apply(worker,(i,))

print("----start----")
po.close() #关闭进程池，关闭后po不再接收新的请求
po.join() #等待po中所有子进程执行完成，必须放在close语句之后
print("-----end-----")

'''
apply(func[, args[, kwds]])：使用阻塞方式调用func
0开始执行,进程号为21532
0 执行完毕，耗时1.91
1开始执行,进程号为21534
1 执行完毕，耗时1.72
2开始执行,进程号为21533
2 执行完毕，耗时0.50
3开始执行,进程号为21532
3 执行完毕，耗时1.27
4开始执行,进程号为21534
4 执行完毕，耗时1.05
5开始执行,进程号为21533
5 执行完毕，耗时1.60
6开始执行,进程号为21532
6 执行完毕，耗时0.25
7开始执行,进程号为21534
7 执行完毕，耗时0.63
8开始执行,进程号为21533
8 执行完毕，耗时1.21
9开始执行,进程号为21532
9 执行完毕，耗时0.60
----start----
-----end-----
'''