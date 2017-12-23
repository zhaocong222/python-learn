class Test(object):
    def __init__(self):
        self.__num = 100
    
t = Test()
print(t.__num)  #报错  __num 私有属性

#前置单下滑线 表示 只能在当前模块使用，import ,from无法导入
_num = 100