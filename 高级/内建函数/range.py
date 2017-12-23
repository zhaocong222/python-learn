a = range(5)
print(a) #返回迭代器
#如果想得到列表,可通过list函数
print(list(a))

#创建列表的另外一种方法
testlist = [x+2 for x in range(5)]
print(testlist)