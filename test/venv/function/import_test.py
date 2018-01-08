#-*- coding:UTF-8 -*-

from make_shirt import get_format_name
zly = get_format_name('Li','sdd','Yunfei')
print(zly)

#列表翻转函数实现
list = ['1','2','3','4','5','6']
list.reverse()
print list

def reverse(names):
    list = []
    while names:
        list.append(names.pop())
    return list

list1=reverse(list)
print list1