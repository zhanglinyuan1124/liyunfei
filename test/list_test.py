# -*- coding: UTF-8 -*-

names = ['liyunfei','yuanyuan','devid','rose']
print names
var0 = names.pop() #默认删除最后一个元素
print var0
print names
var1 = names.pop(2) #删除任意一个位置
print var1

print names

new_names = ['decid','seices','am','pm']
new_names.remove('am')
print new_names

diner = ['luna','AM','PM','TB','CM']
str1 =  '我想要邀请共进晚餐的有'
print diner
print diner.pop(2)+'无法参加晚饭'
diner.append('TD')
print diner
print('我找到了一个更大的餐桌，我想邀请更多的人')
diner.insert(0,'Lyf')
diner.insert(2,'Zly')
diner.append('ZYJ')
print  diner
var1 = diner.pop()
print var1+'抱歉'
var1 = diner.pop()
print var1+'抱歉'
print diner
del diner[2]
print diner

#组织列表的方式 sort永久排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print cars
cars.sort(reverse = True) #逆序排列
print cars

#sorted()临时排序，不改变列表的原有顺序
peoples = ['AX','AC','B','sd','wd']
print peoples
print(sorted(peoples)) #临时排序
peoples.reverse()
print peoples
print(len(peoples)) #列表的长度


