# coding=utf-8
import types


class Car(object):  # Car中定义了私有变量 ‘age’和‘owner’
    def __init__(self, age, owner):
        if type(age) == types.IntType:  # 检测类型是否符合
            self.__age = age
        if type(owner) == types.StringType:
            self.__owner = owner
    # 通过两个函数来获得私有变量的值
    def get__owner(self):
        return self.__owner

    def get__age(self):
        return self.__age


class QQ(object):
    __slots__ = ('__age', 'owner')

    def __init__(self, owner):
        self.owner = owner

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if isinstance(value,types.IntType):
            self.__age = value


myCar = Car(4, 'Tom')
myQQ = QQ('Bill')
myQQ.age = 0
if hasattr(myQQ, 'age'):  # 检测‘myCar’中是否有age
    print myQQ.age
else:
    setattr(myQQ, 'age', 10)  # 如果没有age， 就添加age
    print myQQ.age


