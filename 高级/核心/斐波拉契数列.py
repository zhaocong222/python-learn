def fib(times):
    n = 0
    a,b = 0,1
    while n < times:
        print(b)
        a,b = b,a+b
        n+=1
    return 'done'

#fib(5)

def fib2(times):
    n = 0
    a,b = 0,1
    while n < times:
        yield b
        a,b = b,a+b
        n+=1
    return 'done'

f = fib2(5)
for v in f:
    print(v)