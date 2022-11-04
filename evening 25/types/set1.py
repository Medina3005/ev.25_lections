#  множества в питоне - "контейнер", котрый содержит в себе уникальные элементы в неупорядочном виде 

# {} !!!
# a = {1: 'a'} -> словари
# a = {1, 2, 3} -> множества

# set_ = {1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7}
# print(set_)
# print(type(set_))

# ls = [1, 2, 'a', 0, False, True, 'n', 'b']
# str1 = 'My name is John Snow'
# ls.extend(str1)
# print(ls)
# res = list (set(ls))
# print(res)

# print(ls)
# set1 = {*ls}
# res = [*set1]
# print(set1)
# print(type(set1))
# print(res)
# print(type(res))

#FIFO/lifo - first in first out



# a = {1, 2, 3, 4, 5}
# print(a)
# a.pop()
# print(a)

# remove /discard

# remove -> error
# discard -> None
# set_ = {1, 2, 3, 4, 5, 6, 7}
# set_.discard(5)
# set_.remove(8)
# print(set_)

#frozenset - замороженное множество (неизм тип данных)
# a = {1, 2, 3, 4, 5}
# f_set = frozenset([1,2,3,4,5])
# print(type(a))
# print(type(f_set))
# print(a)
# print(f_set)
# print(dir(f_set))

# a = set('qwerty')
# b = frozenset('qwerty')
# print(1)
# print(a)
# print(1)
# print(b)

# -------------------------------------------

# months = {
#     1: 'January',
#     2: 'February',
#     3: 'March',
#     4: 'April',
#     5: 'May',
#     6: 'June',
#     7: 'Jule',
#     8: 'August',
#     9: 'September',
#     10: 'October',
#     11: 'November',
#     12: 'December'
# }
# while True:
#     number = input('Введите номер месяца:')
#     if number == 'join':
#         break
#     if not number.isdigit():
#         print('Требуется ввести реальный номер месяца!')
#         continue
#     number = int(number)
#     if number not in range(1, 13):
#         print('Требуется ввести реальный номер месяца!')
#         continue

#     if number in range (3, 6):
#         print(f' Вы родились в {months[number]}. Птицы пели прекрасные песни.')
#     elif number in range(6, 9):
#         print(f' Вы родились в {months[number]}Солнце светило ярче чем когда-либо.')
    
#     elif number in range(9, 12):
#         print(f' Вы родились в {months[number]}. Урожай был невероятным.')
#     else:
#         print(f' Вы родились в {months[number]}.За окном падал белый снег.')

        



