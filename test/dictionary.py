# -*- coding: UTF-8 -*-
alien0 = {'color':'green','points':5}
print(alien0)
print(alien0.keys())
print(alien0['color'])

#添加元素
alien0['points_x'] = 0
alien0['points_y'] = 25
print(alien0)

alien1 = {'point_x':2,'point_y':25,'speed':'low'}

if (alien1['speed'] == 'low'):
    x_increm = 1
    y_increm = 2
elif (alien1['speed'] == 'middle'):
    x_increm = 2
    y_increm = 4
elif (alien1['speed'] == 'fast'):
    x_increm = 8
    y_increm = 5

new_alien1 = {}
new_alien1['point_x'] = alien1['point_x'] + x_increm
new_alien1['point_y'] = alien1['point_y'] + y_increm

print(alien1)
print(new_alien1)


#del删除键值对
print(alien0)
del alien0['points_y']
print(alien0)


#使用for循环遍历字典
users = {
    'username':'efiram',
    'first':'li',
    'last_name':'yuenfei',
    'age':'20',
    'major':'programer'
}

for key,value in users.items():
    print("\nKey: " + key)
    print("\nValue: "+ value)
