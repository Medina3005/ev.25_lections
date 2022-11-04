#int, str, bool, dict, list, set, tuple
# name = input('Enter your name:')
# last_name = input('Enter your surname:')
# print('Hello', name, last_name)

# first_num = int(input('Enter first number:'))
# second_num =int (input('Enter second number:'))
# print(first_num + second_num)
# print(type(first_num))
# print(type(second_num))

# a = 4
# b = a if a > 0 else -a
# print(a)

# num = 4
# b = num if num > 0 else -num
# print(num)

# if isHappy and  user_data == 6:
#     print('User is happy')
# elif user_data == 5:
#     print('Number is 5')


# user_data = int(input('Введите число:'))

# if user_data > 5:
#     print('Number is bigger than 5')

# for i in range(1, 6, 2):
#     print(i)

# word = 'Hello word'
# for i in word:
#     print(i)


# count = 0
# word = 'Hello word'
# for i in word:
#     if i == 'l':
#         count += 1
# print('count:' , count)

# цикл for отличается от цикла while тем, что 
# after for we write in 


# while - указываем определнное условие 

# i = 5
# while i <= 15:
#     print(i)
#     i += 2

# isHasCar = True

# while isHasCar:
#     if input( 'Enter data:') == 'Stop':
#         isHascar = False

# for i in range(1, 11):
#     if i >= 5:
#         break

#     if i % 2 == 0:
#         continue

# n = int(input('Enter length:'))

# user_list = []

# i = 0
# while i < n:
#     string = 'Enter element #' + str(i + 1) + ':'
#     user_list.append(input(string))
#     i += 1

# print(user_list)

# word = 'Football, basketball, skate'
# print(word.count('p'))

# print(word.find('p'))
# hobby = word.split(', ')
# print(hobby[0])

# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()

# result = ','.join(hobby)
# print(result)

# word = 'Football'
# print(word[1:-1:])

# list = [6, 4, 'Stroka', True,  6.5]
# print(list[2:5:2])
# print(list[::2])

#-------------------------------------

#Кортежи 

# data = (4, 6, 7, 3, 6, True, 5, 6, 'Hello')
# #data[0] = 5
# print(data[1:5])

# # print(data.count(60))
# # print(len(data))
# print(data)

# data = (4, 6, 7, 3, 6, True, 5, 6, 'Hello')

# for el in data:
#     print(el)

# nums = [5, 7, 8]

# new_data = tuple(nums)
# word = tuple('Hello world')
# print(word)

country = {'code': 'RU', 'name': 'Russian', 'population': 144, 144}
print(country[True])