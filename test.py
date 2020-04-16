"""
a = 123
b = 456.789
c = 1 + 2j
d = 'Hello World'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
"""
"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version: 0.1
Author: chen

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
"""
"""

将华氏温度转换为摄氏温度

"""
"""
f = float(input('请输入华氏温度：'))
c = (f-32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏温度 = {c:.1f}摄氏温度') # 注意单引号前面有个f

"""
"""

输入圆的半径计算圆的周长和面积

"""
# pi = 3.14
# r = float(input('请输入半径：'))
# zhouchang = 2 * pi * r
# mianji = pi * r * r
# print('圆的周长是%.2f' % zhouchang)
# print('圆的半径是%.2f' % mianji)

"""

判断年份是不是闰年

"""
# year = int(input('请输入年份：'))
# is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(is_leap)

"""
用户身份验证

"""
# username = input('请输入用户名：')
# password = input('请输入密码：')
# if username == 'chen' and password == 'wscjy1337':
#     print('用户身份验证成功！')
# else:
#     print('用户身份验证失败！')
"""
分段函数求值

"""
# x = float(input('x = '))
# if x > 1:
#     y = 3 *x -5
# elif x >= -1 and x <= 1:
#     y = x + 2
# else:
#     y = 5 * x +3
# print('f(%.2f) = %.2f' % (x,y))
"""
英制单位英寸和公职单位厘米互换

"""
# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print('输入单位无效！')
"""
百分之成绩转换为等级制成绩

"""
# score = int(input('请输入百分制成绩：'))
# if score >= 90:
#     grade = 'A'
# elif score >= 80 and score <90:
#     grade = 'B'
# elif score >= 70 and score <80:
#     grade = 'C'
# elif score >=60 and score <70:
#     grade = 'D'
# else:
#     grade = 'E'
# print('你的等级制成绩为：', grade)
"""

输入三条边长，判断能否构成三角形，如果能则计算三角形的周长和面积

"""
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c >a:
#     print('周长为：%f' % (a + b +c))
#     p = (a + b +c) / 2                                  # 此为计算三角形面积的
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5     # 公式：海伦公式
#     print('面积为：%f' % (area))
# else:
#     print('三条边不能构成三角形！')
"""

利用for循环实现1到100求和

"""
# sum = 0
# for x in range(101):
#     sum += x
# print(sum)
# # 1到100的偶数求和
# sum1 = 0
# for x1 in range(0,101,2):
#     sum1 += x1
# print(sum1)
"""

猜数字小游戏，猜数字游戏的规则是：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。

"""
# import random
#
# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入一个数字：'))
#     if number < answer:
#         print('大一点')
#     elif number >answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了！')
#         break
# print('你一共猜了%d次' % (counter))
# if counter > 7:
#     print('猜的次数似乎有点多哦！')
"""

九九乘法表

"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d' % (i, j, i*j), end = '\t')
#     print()
"""
输入一个正整数判断它是不是素数

"""
# from math import sqrt
#
# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)
"""
输入两个正整数计算它们的最大公约数和最小公倍数

"""

# x = int(input('x = '))
# y = int(input('y = '))
# # 如果x大于y就交换x和y的值
# if x > y:
#     # 通过下面的操作将y的值赋给x, 将x的值赋给y
#     x, y = y, x
# # 从两个数中较的数开始做递减的循环
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))  # //是整除运算符
#         break
"""
打印三角形图案

"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()