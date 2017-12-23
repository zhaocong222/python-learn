import time
try:
    f = open("test.txt")
    try:
        while True:
            #每次读取一行
            content = f.readline()
            if len(content) == 0-:
                break
            #time.sleep(2)
            print(content)
    finally:
        f.close()
        print("关闭文件")
except Exception:
    print("文件不存在")