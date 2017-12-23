#去重
y = set(['h','e','l','l','o'])
print(y)
print(list(y))

z = set('spam')
print(z)

x = set('abcd')
print(x)

#交集
print(x&z)

#并集
print(x|y)

#差集
print(x-y)

#对称差集 (在x或z中，但不会同时出现在二者中)
print(x^z)