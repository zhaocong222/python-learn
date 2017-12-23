import copy

a = [1,2,3]
b = [4,5,6]
c = [a,b]

print(id(a))
print(id(c))

#深拷贝 , 如果 c 里面引用 a,b 将递归拷贝
d = copy.deepcopy(c)

print(id(c))
#拥有自己的内存空间地址
print(id(d))

#浅拷贝 ，如果c里引用a,b 将不会继续拷贝，只拷贝一层
e = copy.copy(c)
