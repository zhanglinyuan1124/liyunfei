# -*- coding: UTF-8 -*-
cars = ['audi','BMW','subru','toyota']
for car in cars:
    if car == 'BMW':
        print (car.lower())
    else:
        print (car.upper())

if 'audi' in cars: #使用in可以判断一个元素是否存在于一个列表中
    print 'audi in cars'

if 'auDi' not in cars:
    print('auDi not in cars')

game_status = True
if (game_status):
    print 'Game is running!!!'

age = 12
if age < 4 :
    print '4 岁以下的儿童免费'
elif age >= 4 and age <18 :
    print '4~18岁的儿童请付5美元'
else :
    print '15美元才能进入'

dogs = []
if dogs:
    print 'list is null!'
else:
    print dogs


users = ['linu','davide','roses','admin','nomal']
for i in users:
    if (i == 'admin'):
        print 'hello! '+i+',would you like to see a status report?'
    else:
        print 'hello! '+i+',welcome'

while len(users) >0:
    users.pop()

if (users):
    print '删除客户'
else:
    print 'we need more customers'


curusers = ['linu','Davide','roses','admin','nomal']
newusers = ['zouse','davide','Roses','dddd','hello']

new_cur_cus = []
new_new_cus = []

for i in curusers:
    new_cur_cus.append(i.upper())

for i in newusers:
    new_new_cus.append(i.upper())

for i in new_new_cus:
    if i in new_cur_cus:
        print i+' already is used'
    else:
        print i+' can use'


