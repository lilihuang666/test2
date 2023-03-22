# coding=utf-8

class People:
    def __init__(self, name):
        self.name = name


p = People("小红")
# ininstance(对象，类)
print(isinstance(p, People))  # isinstance 判断一个对象是不是一个类的实例或者子类的实例，返回True 或者False
