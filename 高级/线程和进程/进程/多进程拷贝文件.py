import os
from multiprocessing import Pool,Manager

def copyfile(filename,newfilename,queue):
    #完成拷贝一个文件的功能
    fr = open(filename) #读文件
    fw = open(newfilename,"w") #写新文件

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(newfilename)


def main():
    #0. 获取用户要copy的文件夹的名字
    folder_name = input("输入文件夹的名字:")

    #1. 创建一个文件夹
    new_name = 'new_'+folder_name
    #print(new_name)
    #os.mkdir(new_name)

    #2. 获取old文件夹中的所有的文件名字
    fileNames = os.listdir(folder_name)
    #print(fileNames)
    #3. 使用多进程的方式copy 原文件夹中的所有文件到新的文件夹
    pool = Pool(5)
    queue = Manager().Queue()

    for name in fileNames:
        #注意参数这里要写逗号, 传一个元祖
        pool.apply_async(copyfile,args = (folder_name+"/"+name,new_name+"/"+name,queue))

    num = 0
    allnum = len(fileNames)
    while num<allnum:
        queue.get()
        num += 1
        rate = num / allnum
        #end='' 表示不换行
        print("\rcopy的进度是：%.2f%%"%(rate*100),end='')
        
    pool.close()
    #等待进程池中所有任务结束，主进程才结束
    #pool.join()

    print("#\n已完成拷贝")

if __name__ == "__main__":
    main()

