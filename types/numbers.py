#Типы данных - Числа (int), float()




# number = 5 # variable (переменная)
# print(number)
# number = 51 
# print(number)

#tommorow day -> snake case
#tom omorowDay -> Camel case 
# abc  -> нижний регистр 
# ABC -> верхний регистр 

# + 
# num1= 5
# num2 = 15
# result = num1+num2
# print (result) 
#print ( Резултьтат суммы чисел 5 и 15 :),5+15  

#a = 100
#b = 1000
#c = 56.20 # float
#print (a+ b + c)


# -
#num1 = 996 
#num2 = 67.55
#print(num2 - num1)

# *
#num1 = int 
#(input ('Введите число 1:'))
#num2 =  int (input ('Ввудите число 2: '))
#result = num1 * num2
#print('Результат произвеения чисел'), num1, 'и',  num2, 'равно ':, result '

#num = '15' 
#num = float(num) # '15'-> 15
#print (type(num))

# / and // % 
#/-> Обычное деление 
#//-> Целочисленное деление (деление без остатка )
#%-> модуль деление (остаток от деления)

#num1 = 5
#num2 = 2

#print (num1 / num2)
#print (num1 // num2)
#print (numb1 % num2)


# ** -> возведение в степень 


#num1 = 5
#print(num1 ** 1000)


#pow(a,b) -> функция возведения числа а в степень b


# print (pow(2, 5 ,5)) #  2 ** 5 % -> 2

# divmod (a,b) -> Она выводит два числа, первое число это результат целочисленного деления (//) а второе число это модульное деление (%) двух чисел 



#res = divmod (4,5)
# print(res)

#round()-> функция округления числа 

#res = 24 / 13
#print (round (res,1))

#abs() - aбсолютное значение -> abs (-5) = 5 -> |-5| = 5

#print (abs(-100))
#print (abs(50))


#import math 
#print(math.pi)
#math.sqrt-> корень числа 

#print(math.sqrt(25))

#from math import pi, sqrt 

#print(pi)

# from turtle import clear


# clear

# num = float(input("Введите длину стороны квадрата: "))
# print(num * 4, ' - периметр квадрата')
# print(num * num, '-площадь квадрата')



# lenght = float(input('Введите ширину прямоугольника:'))
# height = float(input('Введите длину прямоугольника:'))
# print(lenght * height, -'площадь прямоугольника')


# lenght = int(input("a:= "))
# height = int(input("b:= "))
# print(f'Введите длину и ширину прямоугольника:')
# print("P:= %d; S:= %d." % ((lenght+height)*2, lenght*height))


# num = 4
# p = num * 4
# s = num * num
# print(p, s)

# length = 5
# height = 4
# p = (length + height)* 2
# s = length * height
# print(p, s)


# import math
# class circle():
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * (self.radius**2)
#     def perimeter(self):
#         return 2 * math.pi * self.radius
 
# r = int(input("Введите радиус круга: "))
# obj = circle(r)
# print("Площадь круга:", round(obj.area(), 2))
# print("Длина окружности:", round(obj.perimeter(), 2))

# my_list = [1, 2, 3, 4, 5]
# print(my_list)

import math
radius = int(input('Введите радиус:'))
S = math.pi * radius** 2
p = math.pi * radius
print('Площадь круга :S')
print('Периметр круга: P')