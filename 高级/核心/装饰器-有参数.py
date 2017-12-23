def func(functionName):
    print("----func1---")
    '''
    def func_in(a,b):
        print("-------x1-----------")
        functionName(a,b)
        print("-------x2-----------")
    '''

    #不定长参数传递 (推荐使用这种方式,兼容所有)
    def func_in(*args,**kwargs):
        print("-------x1-----------")
        functionName(*args,**kwargs)
        print("-------x2-----------")

    return func_in

@func
def test1(a,b):
    print("----test-a=%d,b=%d"%(a,b))

test1(11,22)
