# Вам дан файл article.txt
# Требуется реализовать функцию longest_words(filename: str), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько)



# def longest_words(filename):
#     with open(filename) as file:
#         words = file.read().split()
#     words.sort(key=len, reverse = True)    
#     max_len = len(words[0])
#     res = []
#     for i in words:
#         if len(i) == max_len:
#             res.append(i)
#         else:
#             break
#     return res if len(res) > 1 else res.pop()

# print(longest_words('test.txt'))



# 1.Вам дан список accounts, элементами которого являются другие списки
# Каждый список представляет собой количество денег на счету клиента.
# Напишите функцию которая выводит максимальное количество денег на счету самого богатого клиента.

# Пример:
# accounts = [[1,5],[7,3],[3,5]]
# # Ожидаемый вывод: 10

# res = [] #
# for i in accounts:
#     res.append(sum(i)) #[1,5]-> 6,10,8
# print(max(res))
# # выражение
# res = [sum(i) for i in accounts]

# ********************************************************************

# 2.Вам даны две строки:
# Word - слово, ch - буква.
#  Напишите функцию которая будет переварачивать сегмент слова (word),который начинается с индекса 0 и заканчивается индексом первого вхождения ch(включительно). Если ch не существует в слове, возвратите переменную word.

# Пример:
# Ввод: word = "abcdefd", ch= "d"
#  Ожидаемый вывод: "dcbaefd"
# Объяснение:
# Первое вхождение "d" находится в индексе 3.
# Переверните часть слова от 0 до 3 (включительно), в результате получится строка «dcbaefd».

# word = "abcdefd" # -> "dcbaefd"
# ch = "d"
# def func(word, ch):
#     mid = word.index(ch) #3
#     s1 = word[0:mid+1] # abcd [::-1]
#     s2 = word[mid+1:] # efd
#     return s1[::-1]+s2 #
# print(func(word,ch))



# Напишите func которая фильтрует строковые данные в списке.
# Если строка является числом, то преобразуйте его в числовой тип и
# запишите в список, иначе пропустите строку.
# Ввод:
# ['123', '12sd', '54', 'das', '142']
# Вывод:
# [123, 54, 142]


#1def func(l):
    # filtered_list = list(filter(lambda x: x.isdigit()))
    #['123', '12sd', '54', 'das', '142'] #-> [123, 54, 142]
    #res = list(map(lambda x: int(x), filtered_list))
    #2res = list(map(lambda num: int(num), filter(lambda str_: str_.isdigit(), l)))
    # res = [int(i) for i in l if i.isdigit()]
    # res = []
    # for i in l:
    #     if i.isdigit():
    #         res.append(int(i))
    #3return res

#4print(func(['123', '12sd', '54', 'das', '142']))

# list_ = ['123', '12sd', '54', 'das', '142']
# idx = 0
# idx2 = 2
# for i in range(len(list_)):
#     if i == idx or i == idx2:
#         list_.pop(i)
# print(list_)
# for i in range(list_.copy()):



# Дан словарь, удалите из него все элементы с пустыми значениями.
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# a = {'a': 1, 'b': 34, 'c': None, 'd': 5, 'e': None}
# # a <------------- a.copy()
# for i in a.copy(): # 4 iteration
#     if a[i] == None:
#         a.pop(i) # 3
# print(a)