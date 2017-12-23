a = 100
b = 200

def test():
    a = 11
    b = 22
    print(locals())
    print(globals())

test()

#Python 使用 LEGB 的顺序来查找一个符号对应的对象
#locals -> enclosing function -> globals -> builtins

#locals，当前所在命名空间（如函数、模块），函数的参数也属于命名空间

#enclosing，外部嵌套函数的命名空间（闭包中常见）
def fun1():
  a = 10
  def fun2():
      # a 位于外部嵌套函数的命名空间
      print(a)

#globals，全局变量，函数定义所在模块的命名空间

#builtins，内建模块的命名空间。
'''
Python 在启动的时候会自动为我们载入很多内建的函数、类，
  比如 dict，list，type，print，这些都位于 __builtin__ 模块中，
  可以使用 dir(__builtin__) 来查看。
  这也是为什么我们在没有 import任何模块的情况下，
  就能使用这么多丰富的函数和功能了。

  在Python中，有一个内建模块，该模块中有一些常用函数;在Python启动后，
  且没有执行程序员所写的任何代码前，Python会首先加载该内建函数到内存。
  另外，该内建模块中的功能可以直接使用，不用在其前添加内建模块前缀，
  其原因是对函数、变量、类等标识符的查找是按LEGB法则，其中B即代表内建模块
  比如：内建模块中有一个abs()函数，其功能求绝对值，如abs(-20)将返回20。
'''