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
    #Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
    #每次循环将会用空闲出来的子进程去调用目标
    po.apply_async(worker,(i,))

print("----start----")
po.close() #关闭进程池，关闭后po不再接收新的请求
po.join() #等待po中所有子进程执行完成，必须放在close语句之后
print("-----end-----")

'''
apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；
----start----
0开始执行,进程号为21466
1开始执行,进程号为21468
2开始执行,进程号为21467
0 执行完毕，耗时1.01
3开始执行,进程号为21466
2 执行完毕，耗时1.24
4开始执行,进程号为21467
3 执行完毕，耗时0.56
5开始执行,进程号为21466
1 执行完毕，耗时1.68
6开始执行,进程号为21468
4 执行完毕，耗时0.67
7开始执行,进程号为21467
5 执行完毕，耗时0.83
8开始执行,进程号为21466
6 执行完毕，耗时0.75
9开始执行,进程号为21468
7 执行完毕，耗时1.03
8 执行完毕，耗时1.05
9 执行完毕，耗时1.69
-----end-----
'''