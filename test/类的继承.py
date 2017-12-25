# -*- coding: UTF-8 -*-
class Praent:
    parentAttr = 100
    def __init__(self):
        print "调用父类的构造方法"

    def parentMethod(self):
        print  "调用父类的方法"

    def setAttr(self,attr_value):
        Praent.parentAttr = attr_value

    def getAttr(self):
        print "父类属性:",Praent.parentAttr

class child(Praent):

    def __init__(self):
        print  "调用子类的构造方法"

    def childself(self):
        print "调用子类的方法"

c = child()
c.childself()
c.parentMethod()
c.setAttr(555)
c.getAttr()

print Praent.__dict__
print child.__dict__

# 你可以使用issubclass()或者isinstance()方法来检测。
# issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
# isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。

print isinstance(c,child)
print isinstance(c,Praent)
print issubclass(child,Praent)
print issubclass(Praent,child)