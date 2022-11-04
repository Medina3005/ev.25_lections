# sentence = input('Vvedite predlojeniye:')

# if sentence[-1] == '?':
#     print('предложение вопросительное')
# else:
#     print('Обычное предложение')

# sentence = input('Vvedite predlojenie:')
# print('Предложение вопросительное' if sentence[-1] == '?' else 'Обычное предложение')

# ------------------------------------------------------------------------

# Ternary operator (Турнарный оператор) - конструкция которая аналогична по своим свойствам и действию конрукции if/else , если при этом записывается в одну строчку 
# кода.

# <  если в условии true> if <условие> else < вырвжение если false>

# number = 18
# res = 'even number' if number % 2 == 0 else 'odd number'
# print(res)
# common string operators

# from string import digits 

# symbols = digits + '-' 
# print(symbols)
# number = input('Vvedite chislo: ')
# is_correct = True
# for i in number: #567 #67i
#     if i not in symbols: #0123456789-
#         is_correct = False 


# if is_correct:
#     print('Yes number')
#     number = int(number)
#     print('Your number:', number)
#     result = number if number >= 0 else -number # -(-56)
#     print(result)
# else:
#     print('Invalid values!')
# if number.isdigit():
#     number = int(number)
#     print(number)
#     print('Да число!')

# else:
#     print('Вы ввели не число!')
#-----------------------------------------------------

from string import digits # digits


flag = True
symbols = digits + '-' + '-'

while flag:
    is_correct_number = True
    num1 = input('Vvedite pervoe chislo:')
    if len(num1) <= 1 and (num1 == '.' or num1 == '-') or not num1:
        print('Вы ввели неправильное число')
        is_correct_number = False


    for x in num1:
        if x not in symbols: #i56yu
            print('Вы ввели неправильное число')
            is_correct_number = False
            break
    
    num2 = input('Vvedite vtoroe chislo:')
    if len(num2) <= 1 and (num2 == '.' or num2== '-') or not num2:
        print('Вы ввели неправильное число')
        is_correct_number = False
    for x in num2:
        if x not in symbols: #i56yu
            print('Вы ввели неправильное число')
            is_correct_number = False
            break
    if not is_correct_number:#56 #56y
        continue

    num1 = float(num1) if '.' in num1 else int(num1)  
    num2 = float(num2) if '.' in num2 else int(num2)       
    print(num1)
    print(num2)

    operator = input('Vvedite ,(+, -, *, /): ')

    if operator == '+':
        print(f'Результат: {num1 + num2}')
    elif operator == '-':
        print(f'Результат')
    elif operator == '*' :
        print(f'Результат: {num1 * num2}')
    elif operator == '/':
        if num2 == 0:
            print('На ноль делить нельзя!')
        else:
                print(f'Результат: {num1 / num2}')
    else:
        print('ВЫ ввели неправильный оператор!')
    choice = input('Хотите остановить (yes): ')
    if choice.lower() == 'yes':
        flag = False
        print('Пока!')










