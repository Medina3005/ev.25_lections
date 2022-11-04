# text = 'ha ha ha ha'
# result = text.replace('a', 'i', 2)
# print(text)
# print(f' result after replace: {result}')

#str = 'Hello world! My name is John Snow'
#res = str1.replace('John Snow', 'Jamie Lanister')
#res = res.replace('')
#print(res)

# print(id('H))
# print(id('H))
# print(id('h))

# strip() - убирает пробельное символы в начале и в конце строки 
# rstrip, lstrip

# text = input('Enter the text:')
# print(text)
# print(len(text))
# res = text.strip()
# print(res)   
# print(len(res))


# text = '   Hello world   '
# print(len(text))
# res = text.lstrip()
# print(res)
# print(len(res))

# print(dir(str))




# isdigit ->                   проверяют 
# isnumeric -> ->  состоит ли наша строка полностью из чисел
# isdecimal ->

# text = '572777'
# if text.isdigit():
#   num = int(text)
#   print(num)
# else:
#     print('Oops! Invalid symbols!')


# text = '\u0031' 
# print(text)
# print(text.isnumeric())

#isalnum() -> проверяет состоит ли наша строка из чисел и символов латинского алфавита и киррилицы

# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

 #isalpha() -> состоит ли наша строка полностью из символов латинского либо киррильского алфавита

# text ='Hello world'
# print(text[:5].isalpha())

# islower()
# isupper()
# istitle()

# index(value, [start],[end]) -> выводит индекс значения value котрое мы передаем в нашей строке.

# count(value,[start]) -> считает количество вхождений value в нашу строку

# text = 'hello 0 0 hello'
# print(text.count('hello'))
# print(text.count('o'))
# print(text.count(' '))

# text = 'Hello world! My name is John Snow'
# print(text.index('John'))
# res = text.index('o')
# print(res)
# res = text.index('0, res+1')
# print(res)
# res = text.index('0, res+1')
# print(res)
# res = text.index('0', res+1)
# print(res)

#text = 'ooohello world! Myo name is John Snowooo'
# text = input('Enter the text:')
# i = 0
# res = -1
# while i < text.count('o'): # 4
#     res = text.index('o', res+1)
#     print(res)
#     i += 1 #инкремент i = i + 1 # i++


# find(value,[start], [end]) -> делвет тоже самое что и index,  но есть одно отличие в том что если value нет  в строке то возвращается index -1

# text = 'Hello'
# print(text.find('l'))
# print(text.index('hi'))

# swapcase() -> переводит все символы в противоположный регистр 
# upper()-> все символы в верхний регистр
# lower()-> все символы в нижний регистр

# text = 'hello World, joHN, SNow'
# print(text.swapcase())
# print(text.upper())
# print( text.lower())


#capitalize()- переводит первую букву в верхний регистр

# name = input('Enter your name:').capitalize()
# print( f'Hello! Mr/Mrs {name}!')

#title()-> переводит первые символы всез слов в верхний регистр
# text ='John jamie sansa nursultan jerry'
# print(text.title())
# print(text.capitalize())

# name = input('Vvedite FIO:')
# print(name.title())

#split(разделитель)- дробит строку на несколько частей  по разделителю который находится в строке, все части строки сохранются в тип данных list

# text = 'Let me speak  by my hearth in English! Cause My name is John Snow!'
# ls = text.split(' ')
# print(ls)
# print(len(ls))

# #'разделитель' .join(iterable(list)) -> соединяет по разделителю строки которые находятся в list

# res = '#'.join(ls)
# print(res)



