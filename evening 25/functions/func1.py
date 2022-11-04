#Функции - это именованная часть программы , которая может вызываться в других частях программы , столько раз , сколько нужно

#def name_of_function(<a, b> # параметры):
# <body> - код , какая то логика, которая будет запусаться при обращении к функции 
#[<return>]оператор для возвращения результата

#name_of_function(5, 6 #аргументы)

# Параметры функции - переменныу которые будет принимать ваша  функция , для того чтобы мы смогли работать с данными , которые 
#попадают в нашу функцию , данные сохраняются в параметрах.

# Аргументы - это данные , которые мы передаем для параметров при вызове функции.

#return - это оператор ,который нужен чтобы функция возвращала результат , если return нет в функции , функция по умолчанию возвращает None.

# res = print('Hello')
# print(res)

# res = max(range(1, 100))
# print(res)

# def sum_two_nums(num1, num2):# параметры
#     result = num1 + num2
#     return result

# res = sum_two_nums(5, 6)
# print(res)

# def our_len(a):
#     try:
#         res = 0
#         for x in a:
#             res += 1
#         return res
#     except TypeError:
#         return 'Value is not iterable!'

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
# str1 = 'Hello world! My name is John Snow!'
# print(our_len(ls))
# print(our_len(str1))
# print(our_len(True))

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     return False

# b = int(input('Vvedite chislo:'))

# print(isEven(15))
# print(isEven(b))
# print(isEven(24))
# print(isEven(98))

# def get_polindroms(words):
#     result = []
#     for x in words:
#         if x.lower() == x[::-1].lower():
#             result.append(x)
#     return result

# some_words = ['John', 'ono', 'Kazak', 'peter', 'Dovod', 'tenet', 'anna', 'kak', 'piko']
# polindroms = get_polindroms(some_words)
# print(polindroms)



