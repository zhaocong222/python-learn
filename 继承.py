#继承
class Animal:
    def eat(self):
        print("---吃---")
    def drink(self):
        print("---喝----")
    def brak(self):
        print("狂怒")

#继承
class Dog(Animal):
    def bark(self):
        print("----汪汪叫----")
        super().brak()

wangcai = Dog()
wangcai.bark()
wangcai.eat()

#调用顺序
print(Dog.__mro__)