# --*-- coding:UTF-8 --*--
prompt = "plese tell me your age\n"
str = ''
while str != 'quit':
    age = input(prompt)
    if age < 3 :
        print 'free'
    elif age >= 3 and age < 12:
        print '10美元'
    elif age >=12 :
        print '15美元'
    str = input("是否结束？/n")



