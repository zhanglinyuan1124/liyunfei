#-*- coding:UTF-8 -*-

class Restaurant(object): #继承时，此处需要添加object
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

class Hotel(Restaurant):
    '''酒店属于特殊的产听'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化父类的属性'''
        super(Hotel,self).__init__(restaurant_name,cuisine_type)
        self.size = 100
        self.address = 'china' #定义新的量

    def describe_restaurant(self):
        '''重写父类的方法'''
        print(self.restaurant_name+' at '+self.address)



myhotel = Hotel('Li','Yunfei')
print(myhotel.cuisine_type)

myhotel1 = Hotel('Li','Yunfei')
myhotel1.size = 300
print(myhotel1.size)
myhotel1.describe_restaurant()


class IceCreamStand(Restaurant):
    '''冰淇淋点'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化父类的属性'''
        super(IceCreamStand,self).__init__(restaurant_name,cuisine_type)
        self.flavors=['caomei','bannana']

    def show_icecream(self):
        print self.flavors

icecream = IceCreamStand('hejiahuan','chaina')
icecream.show_icecream()