l = [x*2 for x in range(5)]
print(l)

for item in l:
    print(item)


#生成器
g = (x*2 for x in range(5))
print(g)

# next() 函数获得生成器的下一个返回值
#print(next(g))
#print(next(g))

#for循环
for item in g:
    print(item)

