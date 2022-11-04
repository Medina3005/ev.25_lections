# ls = [2, '2', '4', 4, 45, '101']
# res = [x**2 for x in filter(lambda x: type(x) == int, ls)]
# res1 = [x**2 for x in ls if type(x) == int]
# print(res)
# print(res1)

#------------------------------------------------------------------------

# from random import choices
# from string import ascii_letters as letters, digits
# from itertools import repeat
# from statistics import mean

# q_pass = int(input('Vvedite kol-vo paroley:'))
# symbols = '_$()-'
# res = {f(choices(letters,k= 10), choices(digits,k= 5), choices(symbols,k=1)) for f in repeat(lambda x, y, z:''.join(set(x+y+z)), q_pass)}
# print(res)
# print(f'Quantity:{len(res)}')
# lens = [len(x) for x in res]
# print(f'Average len of passwords:{mean(lens)} ')


# """1) Дан список, со строками. Отфильтруйте
# этот список, оставив только те строки, длина
# которых больше 7 символов.

# 2) Вам дано три числа(имеется в виду создать
# 3 переменные с числовыми значениями),
# используйте условные операторы и выведите на
# экран наибольшее из них.

# 3) Дан список с числами. Посчитайте
# количество чётных и нечётных чисел в этом
# списке.
#3()
# a = [1, 2, 6, 1, 8, 4]
# chet = 0
# nechet = 0
# for i in a:
#     if i % 2:
#         chet += 1
#     else:
#         nechet +=1
#     print(f'Четных: {chet}, нечетных: {nechet}')

# 4) Дана строка распечатать true если она является палиндромом и. false если не является
# (Палиндро́м, пе́ревертень — число,
# буквосочетание, слово или текст, одинаково
# читающееся в обоих направлениях. Например,
# число 101; слова "кок", "топот", "комок" и
# т.д.)

# 5) Дан список list_ = [-1, 2, 3, 0, 5, -3,
# 7,]. Если число в списке меньше 0, замените
# его на False, если больше, то на True"""

# 1()
# list_ = ['Darica', 'Sanjar', 'Medina', 'Aiziiireeek' 'Oleg', 'Nurayimm']
# list2 = [x for x in list_ if len(x) > 7] # list comprehension
# print(list2)


# list1 = []
# for x in list_: # цикл for 
#     if len(x) > 7:
#         list1.append(x)
# print(list1)

# 2()

# a = 8
# b = 3
# c = 2

# if a>b and a>c:
#     print(a)

# my_str = 'medinam'
# print(my_str[1:6:2])

# str = 'medinam'
# print(str.replace('a', 'k'))


# string = 'hello everyone'
# repeat = string * 3
# print(repeat)

# string = '\nhello everybody'
# res = string*3
# print(res)

# name = input('имя: ')
# last_name = input('фамилия:' )
# age = input('возраст: ')
# city = input('город: ')
# print(f'Вас зовут {name} {last_name}, Ваш возрат {age}, Вы проживаете в городе {city}')



string = 'aolpengold'
print(string.replace(string[1], 'K', 2))