#-*- coding:UTF-8 -*-
class Restaurant(object):
    '''创建一个名为餐馆的类'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''描述餐馆信息'''
        print(self.restaurant_name + ' is '+self.cuisine_type)

    def open_restaurant(self):
        '''餐馆正在营业'''
        print(self.restaurant_name+' is opeing')

restaurant = Restaurant('KFC','quick')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

class User():
    '''创建一个User类'''
    def __init__(self,first_name,last_name):
        '''初始化'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = 12
        self.sex = 'man'
        self.login_attemp=0

    def describe(self):
        '''描述'''
        print(self.first_name+' '+self.last_name+' ,age is '+str(self.age)+',sex is '+self.sex)

    def greer(self):
        '''问候用户'''
        print('hellow,'+self.first_name+' '+self.last_name)

    def increm_login_attemp(self):
        '''尝试登陆次数，每次加1'''
        self.login_attemp = self.login_attemp+1
        print(self.login_attemp)



user1 = User('Li','Yunfei')
user1.describe()

user2 = User('Zhang','Linyuan')
user2.age = 13
user2.sex = 'women'
user2.describe()
user2.increm_login_attemp()
user2.increm_login_attemp()
user1.increm_login_attemp()


