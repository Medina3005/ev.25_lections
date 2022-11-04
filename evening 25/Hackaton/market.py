from product import list_, retrieve_, create_, update, delete_

def main():
    print('Привет ! Тебе доступны следующие функции маркет - плейса: \n\tCreate-1\n\tListing-2\n\tRetrieve-3\n\tUPDATE-4\n\tDELETE-5')
    choice = input('Введите действие(1,2,3,4,5):')


    if choice.strip() == '1':
        print(create_())
    elif choice.strip() == '2':
        print(list_())
    elif choice.strip() == '3':
        print(retrieve_())
    elif choice.strip() == '4':
        print(update())
    elif choice.strip() == '5':
        print(delete_())
    else:
        print('Неверный выбор!')

    answer = input('Хотите продолжить? (yes/no) ')
    if answer.lower().strip() == 'yes':
        main()
    else:
        print('Пока Пока!')

main()


