#-*- coding:UTF-8 -*-
def make_shirt(size,describe="ssss"): #默认值必须放在最后面
    print("T-shirt size is ")+str(size)
    print("describe is ")+describe

shirt1 = make_shirt(2,"i love LGD")
shirt2 = make_shirt(size=2)

def get_format_name(first_name,middle_name,last_name):
    '''返回整洁的名字'''
    if middle_name:
        full_name = first_name + ' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()

lyf = get_format_name('Li','','Yunfei')
print(lyf)

#返回一个字典
def build_person(first_name,last_name):
    '''返回一个名字字典'''
    dir1 = {'first_name':first_name,'last_name':last_name}
    return dir1
test1 = build_person('li','yunfei')
print test1

#象函数传递一个列表
def greet_user(names):
    '''问候列表中的用户'''
    for name in names:
        print "good moning "+name

names = ['liyunfei','linyuan','yy']
greet_user(names)

#3D打印模拟
unprinted = ['iphone','apple','sunsing','iusu']
newprinted = []

while unprinted:
    current = unprinted.pop()
    print current
    newprinted.append(current)

for i in newprinted:
    print i

#传递任意数量的实参
def make_pizza(*topping):
    print (topping)

make_pizza('ss','dd','ssd')
make_pizza('sdd','aasd','sdddf','sss')


