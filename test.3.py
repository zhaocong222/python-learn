#匿名函数
func = lambda a,b:a+b

res = func(1,2)
#print(res)

stus = [
    {"name":"zhangsan","age":18},
    {"name":"lisi","age":19},
    {"name":"wangwu","age":17}
]

stus.sort(key = lambda k:k['name'])

print(stus)