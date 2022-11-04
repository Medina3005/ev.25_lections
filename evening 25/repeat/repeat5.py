# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
#  и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, 
#  что задано положительное целое число). 
# Протестируем функцию на файле «article.txt» со следующим содержимым:

# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


# def read_lines(lines, file):
#     if lines > 0:
#         with open('article.txt', 'r') as file:
#            data = file.readlines()[::-1]
#            for i in range(0, lines):
#             try:
#                 print(data[i].strip())
#             except IndexError:
#                 print('Строки закончились!')
#                 break
#     else:
#         print('Количество строк должно быть положительным!')

# read_lines(3, 'article.txt')
# read_lines(-4, 'article.txt')
# read_lines(10, 'article.txt')

#******************************************************

# Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
# – № - номер по порядку (от 1 до 300);
# – Секунда – текущая секунда на вашем ПК;
# –  Микросекунда – текущая миллисекунда на часах.
# На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды

# import csv
# from  datetime import datetime
# from time import sleep



# with open('rows_300.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['№', 'Hours', 'Minutes', 'Seconds', 'Microseconds'])
#     for x in range(1, 301):
#         print(x)
#         hours = datetime.now() .hour
#         minutes = datetime.now().minute
#         seconds = datetime.now().second
#         microsec = datetime.now().microsecond
#         writer.writerow([x, hours, minutes, seconds, microsec])
#         sleep(0.1)

#########################################################################

# 1. У нас есть файл file.txt c тестом на латинице. Нужно написать программу, которая будет выводить статистику по тексту:

#     > количество букв латинского алфавита
#     > число слов
#     > число строк

# with open('file.txt', 'r') as file:
#     data = file.read()
#     print(data)
#     letters = sum(map(str.isalpha, data))
#     words = len(data.split())
#     file.seek(0)
#     # print(words)
#     lines1 = len(file.readlines())
#     lines2 = data.count('\n') + 1
#     # print(lines1)
#     # print(lines2)
#     print('Input file contains:')
#     print(f'{letters} - letters!')
#     print(f'{words} - words!')
#     print(f'{lines1} - lines!')
######################################################################
 
# """Напишите программу, которая получает на вход строку с названием текстового файла, и выводит
#  на экран содержимое этого файла, заменяя все запрещенные слова звездочками 
#  * (количество звездочек равно количеству букв в слове). Запрещенные слова, 
#  разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
#   Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, 
#   где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: 
#   если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и 
#   exAm должны быть заменены на ****.
# """

# # Input: "Hello, world! Python IS the programming language of thE future. My EMAIL is....
# # PYTHON is awesome!!!!"

# # Output: *, *ld! ****  * programming language of * future. My *** **....
# # ** ** awesome!!!


# with open('forbidden_words.txt') as forbidden_file, open('input.txt') as text_file:
#     forbidden_words = forbidden_file.read().split() 
#     text =  text_file.read()
#     print(forbidden_file)
#     print(text)
#     text_lower = text.lower()
#     for word in forbidden_words:
#         text_lower = text_lower.replace(word, '*' * len(word))
#         # print(text)
#         # print()
#         # print(text_lower)

#         # result = [ x if x == '*' else  for x, y in zip(text_lower, text)] # True = 1
#         result = [(y, x)[x == '*'] for x, y in zip (text_lower, text)]
#         print(''.join(result))
