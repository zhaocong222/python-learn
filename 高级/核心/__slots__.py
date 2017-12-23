class Person(object):
    __slots__ = ("name","age")

p = Person()
p.name = "老王"
p.age = 20

#AttributeError: 'Person' object has no attribute 'score'
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
p.score = 100