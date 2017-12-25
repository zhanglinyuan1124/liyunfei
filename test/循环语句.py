# -*- coding:UTF-8 -*-
#while循环

numbers = [12,37,5,42,8,3]
event = []
odd = []
i = 0
j = 0
while len(numbers) > 0 :
    number = numbers.pop()
    if (number % 2 == 0):
        event.append(number)
    else:
        odd.append(number)

print event
print odd

# while len(event) > 1:
#     print event[1]
#     del event[1]
#
#
# while len(odd) > 1:
#     print odd[1]
#     del odd[1]



#continue 和 break
i = 1
while i < 10:
    i = i + 1
    if i%2 <> 0 :
        continue
    print i

j = 1
while j < 10:
    j = j +1
    if j%2 <> 0:
        break
    print j

# #无限循环
# var = 1
# while var == 1:
#     num = raw_input("ssss")
#     print "number is",num
# print 'goodby'


#循环使用else
count = 1
while count < 5:
    print count
    count = count + 1
else :
    print  count,"is not less 5"

# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 九九乘法表

# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 九九乘法表

i = 1
while i:
    j = 1
    while j:
        print j, "*", i, " = ", i * j, '  ',
        if i == j:
            break

        j += 1
        if j >= 10:
            break

    print "\n"
    i += 1
    if i >= 10:
        break




denum = input("输入十进制数:")
print denum,"(10)",
binnum = []
# 二进制数
while denum > 0:
    binnum.append(str(denum % 2)) # 栈压入
    denum //= 2
print '= ',
while len(binnum)>0:
    import sys
    sys.stdout.write(binnum.pop()) # 无空格输出print ' (2)'