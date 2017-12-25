# -*- coding: UTF-8 -*-
heros = ['zeus','Sven','Naga','Luna','Panda','Enigma']
for i in heros:
    print (i)+'is a Dota hero'
print(len(heros))

for i in range(1,5):
    print i

numbers = list(range(1,9,2))
print numbers

#将1~10的平方进行打印
sqrts = []
for t in range(1,11):
    sqrts.append(t**2)
print(sqrts)

#对数字列表进行简单的统计计算
digits = list(range(1,100,7))
print(digits)
print(min(digits))
print max(digits)
print sum(digits)

#列表解析
digits = [value**2 for value in range(1,11)]
print(digits)

lists = range(1,10000000,3)
print min(lists)
print max(lists)
print sum(lists)

#list 解析联系
num_list = [i**3 for i in range(1,10)]
print num_list


#使用列表的一部分,称为python切片
players = ['chaits','martins','michael','florence']
print players[0:2]
print players[3:]
print players[:2]
new_player = players
print new_player


##a元祖，用来存不可变的值
dimensions = (2,1,3,4,5,2)
print dimensions

#git测试