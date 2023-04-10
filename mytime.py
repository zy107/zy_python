# -*- coding: utf-8 -*-
# 一、定义名为MyTime的类，其中应有三个实例变量 时hour 分minute 秒second
# 1）为了给对象初始化赋值，编写构造方法，对时分秒附初始值
# 2）为了保证数据的安全性，这三个成员变量应声明为私有、
# 3）对三个属性分别定义封装get和set方法，定义一个main方法，创建一个MyTime类的对象并调用这六个方法。
class MyTime:
    def __init__(self,h,m,s):
        self.__h = h
        self.__m = m
        self.__s = s
    def get_h(self):
        return self.__h
    def get_m(self):
        return self.__m
    def get_s(self):
        return self.__s
    def set_h(self,h):
        self.__h = h
    def set_m(self,m):
        self.__m= m
    def set_s(self,s):
        self.__s=s
if __name__ == '__main__':
    s = MyTime(3,28,50)
    print(s.get_h())
    print(s.get_m())
    print(s.get_s())
    s.set_h(6)
    print(s.get_h())
    s.set_s(10)
    print(s.get_s())
    s.set_m(22)
    print(s.get_m())