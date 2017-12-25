#coding=utf-8
#author='lyf'
#数字类型
#int ,long ,float ,complex
var1,var2,var3 = 10,-10,0x69
var4 = 0122L
var5,var6 = 0.1,32.3e+18
var7 = 3e+26J

print var1
print var2
print var3
print var4
print var5
print var6
print var7

#字符串是有数字、字母、下划线组成的一串字符
s = "ilovepython"
print s[1:5] #下标从0算起，不包括上边界
print s[1]
print s[1]+"TEST"
print s[1:4] * 2

# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
# 列表用 [ ] 标识，是 python 最通用的复合数据类型。
# 列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
# 加号 + 是列表连接运算符，星号 * 是重复操作
list = ['liyunfei','yuanyuan','python','C++',var1]
mylist = ['检查','ss']
print list
print list + mylist
list[2] = 111 #列表可重新赋值
print list

# 元组是另一个数据类型，类似于List（列表）。
# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ('liyunfei','yuanyuan','python','C++',10)
print tuple
print tuple[1:2]
print tuple[1:3]
#tuple[1] = 'ssss' #元组不能重新赋值

# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成

dict = {}
dict[1] = 'This is one'
dict['ss'] = 'This is ss'
mydict = {'name':'lyf','age':'23'}
print mydict.keys()
print mydict.values()
print mydict['name']

print mydict.clear()
print mydict
