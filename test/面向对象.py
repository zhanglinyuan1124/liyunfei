# -*- coding: UTF-8 -*-
class Employee:
    # empCount
    # 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用
    # Employee.empCount
    # 访问。
    '所有员工的基类'
    empcount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

        # 第一种方法__init__()
        # 方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法

    def displayCount(self):
        print "Total Employee %d" % Employee.empcount

    def displayEmployee(self):
        print "Name :" ,self.name,",Salary:",self.salary


# "创建 Employee 类的对象"
emp1 = Employee("Zara","20000")
emp2 = Employee("JATA","2222")
emp1.age = 7

emp1.displayEmployee()
emp2.displayEmployee()


# __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
# __doc__ :类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
# __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
#


print Employee.__doc__
print Employee.__dict__
print Employee.__name__
print Employee.__module__
print Employee.__bases__


# Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
# 在 Python 内部记录着所有使用中的对象各有多少引用。
# 一个内部跟踪变量，称为一个引用计数器。
# 当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"


pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)  # 打印对象的id
del pt1
del pt2
del pt3
