# __del__方法

class Dog:
    def __del__(self):
        print("阵亡")

dog1 = Dog()
dog2 = dog1
del dog1
del dog2