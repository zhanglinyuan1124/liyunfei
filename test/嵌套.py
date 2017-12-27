# --*-- coding:UTF-8 --*--

#列表中存储字典
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

alien_s = [alien_0,alien_1,alien_2]

for alien in alien_s: #输出了每个字典
    print alien

#创建30个外形人
alies = []
for alien_number in range(1,30):
    new_alien = {'color':'green','ali_number':alien_number,'points':alien_number,'speed':'slow'}
    alies.append(new_alien)

#显示前5个外星人
for i in alies[:5]:
    print i

#修改外形人的属性
i = 0
for alien in alies:
    if i <= 3 :
        alien['color'] = 'yellow'
        alien['speed'] = 'slow'
        i = i+1
    elif i > 3 and i <= 10 :
        alien['color'] = 'red'
        alien['speed'] = 'middle'
        i = i + 1
    else :
        alien['color'] = 'block'
        alien['speed'] = 'quick'
        i = i + 1
for alien in alies:
    print alien

#字典中存储列表
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheeese']
}

print pizza['toppings']

for i in pizza['toppings']:
    print i