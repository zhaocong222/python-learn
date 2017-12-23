class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge
    
lw = Person("老王",10)

print(lw.age)
print(lw.name)

#添加属性
Person.num = 20

print(lw.num)


#添加方法
def run(self):
    print("------%s正在跑-------"%(self.name))
    

'''
lw.run = run
#虽然p1对象中 run属性已经指向了函数run,但是这句代码还不正确
#因为run属性指向的函数是后来添加的，即 lw.run的时候没有把lw当作第一个参数
#TypeError: run() missing 1 required positional argument: 'self'
lw.run()
'''

#对象添加方法
import types
lw.run = types.MethodType(run,lw)
lw.run()