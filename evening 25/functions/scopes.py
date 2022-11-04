# Область видимости и пространства имен (scopes)
# - 'Это технология которая определяет контекст переменной, в рамках которого мы можем ее использовать и видеть'

# built-in (Встроенная) - print(), len(), math, random, max() etc.

#global(Глобальная область видимости)- это имена, которые определяются в самом файле который вы запускаете.

#*enclosed(nonlocal, не локальная) вложность 

#local(локальная область видимости) - определяется внутри функций


# x = 200

# def func():
#     #print(x)
#     x = 500
#     print(x)
# print(x)
# func()


# a = 10 # global
# print #built in 
# def hello(): # name 'hello' -> global
#     a = 'Hello world' # local
#     print(a, 'local name inside function')
# hello()
# print(a, 'global')

# x = 'global'
# print(x, '1', 'global')

# def enclosed(): # global
#     x = 'enclosed'
#     def local(): # enclosed
#         x = 'local' # local
#         print(x, '3', 'local')
#     print(x, '2', 'enclosed')
#     local()
#     print(x, '4', 'enclosed')

# enclosed()
# print(x, '5', 'global')


# LEGB
#local - enclosed - global -  built in 

# print(len)
# len = 5
# print(len)

# a = 10
# def func():
#     print(a)
#     a = 15
#     print(a)

# func()

# var = 100
# def increment():
#     var = var + 1 # try to update global name inside local scope
#     print(var)
# increment()

#global - оператор , который позволяет изменять значение глобальной переменной , находясь в локальной области видимости

#nonlocal - который позволяет изменять значение не локальной (замкнутой) переменной , находясь в локальной области видимости

# scores = 67


# def increment():
#     global scores
#     scores += 1

# def kill_user():
#     print('Вы убили бота + 1 очко')
#     increment()

# def kill_bot():
#     print('Вы убили персонажа, +1 очко')
#     increment()

# def eat_Edems_apple():
#     print('Вы сьели яблоко Эдема, + 1 очко')
#     increment()

# print('Стартовые очки', scores)
# kill_user()
# kill_user()
# kill_bot()
# eat_Edems_apple()
# kill_bot()
# print('Финальные очки:', scores)

#------------------------------------------------------------------------

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# steps = counter()
# eat = counter()
# print(eat())
# print(steps())
# print(steps())
# print(steps())
# print(steps())
# print(steps())
# print(steps())
# print(eat())

# steps = counter()
# eat = counter()
# total = None
# for i in range(2500):
#     total = steps()

# print(f'За день пройдено{total} шагов!')

#------------------------------------------------------


# globals() -> Возвращает словарь в котором описаны все имена, которые содержат глабальное пространство 

# locals() - > возвращает словарь в котором описаны все имена , которые содержат локальное простанство.

# print(globals())
# print()
# print()
# print(locals())
