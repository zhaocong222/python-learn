#把函数当成生成器用
def fib(n):
    a,b,s = 0,1,0
    while s < n:
        a,b = b,a+b
        s = s + 1
        yield b

'''
a = fib(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''

for v in fib(5):
    print(v)