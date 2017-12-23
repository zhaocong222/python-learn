def func(functionName):
    print("----func1---")

    def func_in():
        print("-------x1-----------")
        xxx = functionName()
        print("-------x2-----------")
        return xxx
    return func_in

@func
def test1():
    print("----test-----")
    return "haha"

ret = test1()
print("xxx is %s"%ret)
