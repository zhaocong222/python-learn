'''
class Test(object):
    def __init__(self):
        self.__num = 100
    
    def setNum(self,newNum):
        print("---setter---")
        self.__num = newNum
    
    def getNum(self):
        print("---getter---")
        return self.__num

    num = property(getNum,setNum)
    
t = Test()

t.num = 200
print(t.num)
'''

#另一种方式利用装饰器
class Test(object):
    def __init__(self):
        self.__num = 100
    
    #注意 这里定义的 num,所以外面调用也要 使用 num
    @property
    def num(self):
        print("---getter---")
        return self.__num

    @num.setter
    def num(self,newNum):
        print("---setter---")
        self.__num = newNum

t = Test()

t.num = 200
print(t.num)