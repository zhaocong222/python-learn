import os

#1.获取一个要重命名的文件夹名字
folder_name = input("请输入要重命名的文件夹:")

#2. 获取那个文件夹中所有的文件名字
file_names = os.listdir(folder_name)

#print(file_names)

for name in file_names:
    #print(name)
    old_file_name = './'+folder_name+"/"+name
    new_file_name = './'+folder_name+"/【zc出品】"+name
    os.rename(old_file_name,new_file_name)