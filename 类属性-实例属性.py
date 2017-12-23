#类属性和实例属性
class Tool(object):

    #类属性
    total = 0

    #静态方法
    @classmethod
    def say(self):
        print("hello world")

    def __init__(self,new_name):
        #实例属性
        self.name = new_name
        #类属性
        Tool.total += 1

tool1 = Tool("a1")
tool2 = Tool("a2")
tool3 = Tool("a3")

print(tool1.name)
print(tool2.name)
print(tool3.name)

print(Tool.total)

Tool.say()