import time
import os

g_num = 100
ret = os.fork()

#变量不共享
if ret == 0:
    print("---process-1-----")
    print(""---process-1---g_num=%d--"%g_num)
    g_num += 1
else:
    time.sleep(3)
    print("---process-2-----")
    print(""---process-2---g_num=%d--"%g_num)