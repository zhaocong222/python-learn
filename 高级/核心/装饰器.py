'''
#利用闭包方法  - 费脑
def check(func):
    def inner():
        print("正在验证权限")
        func()
    return inner

def f1():
    print("---f1---")

def f2():
    print("---f2---")
    
#f1需要验证
f1 = check(f1)
f1()
'''

#利用装饰器
def check(func):
    def inner():
        print("正在验证权限")
        func()
    return inner

#相当于f1 = check(f1)
@check
def f1():
    print("---f1---")

@check
def f2():
    print("---f2---")

f1()
f2()