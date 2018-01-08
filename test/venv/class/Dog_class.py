#-*- coding:UTF-8 -*-
class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age
        self.color = 'yellow'

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print (self.name.title()+' is now sit')

    def roll_over(self):
        '''模拟小狗正在打滚'''
        print(self.name.title()+' is rolled over!')

mydog=Dog('While',6)

print(mydog.name)
mydog.color = 'red'
print(mydog.color)

mydog.sit()