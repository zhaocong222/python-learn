try:
    #11/0
    print("------")
except (NameError, FileNotFoundError):
    print("如果捕获到异常后做的 处理....")
except Exception as ret:
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常，这个execpt一定买个会捕获到")
else:
    print("没有异常才会执行")
finally:
    print("------finally------") 

print("-------2-----------")