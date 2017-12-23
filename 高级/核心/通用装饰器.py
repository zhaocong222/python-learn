#通用装饰器格式
def func(functionName):

    def func_in(*args,**kwargs):
        xxx = functionName(*args,**kwargs)
        return xxx
    #一般情况下为了让装饰器更通用，可以有return
    return func_in

@func
def test1():
    print("----test-----")
    return "haha"

@func
def test2():
    print("----test-----")

@func
def test3(a,b):
    print("----test-----")

ret = test1()
print("xxx is %s"%ret)

test2()
test3(1,2)