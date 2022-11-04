import json

DATA_JSON = '/home/medina/Desktop/evening 25/Hackaton/data.json'
ID_TXT = '/home/medina/Desktop/evening 25/Hackaton/id_data.txt'

def get_data():
    with open(DATA_JSON) as file:
        return json.load(file)

def save_data(data):
    with open(DATA_JSON, 'w') as file:
        json.dump(data, file)

# --------------------------------------

def list_():
    data = get_data()
    return f'Список ноутбуков: {data}'

def retrieve_():
    data = get_data()
    try:
        id = int(input('Введите номер ноутбука: '))
        product = list(filter(lambda x: id == x['id'], data))
        return product
    except:
        return 'Введите правильный номер!'

def get_number():
    with open(ID_TXT, 'r') as file:
        id = int(file.read())
        id += 1
    with open(ID_TXT, 'w') as file:
        file.write(str(id))
    return id

def create_():
    data = get_data()
    try:
        product = {
            'id': get_number(),
            'brand': input('Введите бренд ноутбука: '),
            'model': input('Введите модель ноутбука: '),
            'year': int(input('Введите год выпуска: ')),
            'description': input('Введите описание ноутбука: '),
            'price': round(float(input('Введите цену ноутбука: ')), 2)
        }
    except:
        return 'Введите правильные данные!'

    data.append(product)
    save_data(data)
    return 'Товар успешно добавлен!'

def update():
    data = get_data()
    try:
        id = int(input('Введите номер товара: '))
        product = list(filter(lambda x: x['id'] == id, data))[0]
        print(f'Товар для обновления: {product["brand"]}')
    except:
        return 'Неверный номер товара!'

    index = data.index(product)
    choice = input('Что вы хотите изменить? (1 - brand, 2 - model, 3 - price, 4 - description)')
    if choice.strip() == '1':
        data[index]['brand'] = input('Введите новое название: ')
    elif choice.strip() == '2':
        data[index]['model'] = input('Введите новую модель ноутбука: ')
    elif choice.strip() == '3':
        data[index]['price'] = round(float(input('Укажите новую цену для ноутбука: ')), 2)
    elif choice.strip() == '4':
        data[index]['description'] = input('Введите новое описание для ноутбука: ')
    else:
        return 'Вы ввели неверные данные для обновления товара!'

    save_data(data)
    return 'Товар успешно обновлен!'

def delete_():
    data = get_data()
    try:
        id = int(input('Введите номер ноутбука: '))
        product = list(filter(lambda x: x['id'] == id, data))[0]
        print(f'Товар для удаления: {product["brand"]}')
    except:
        return 'Неверный номер!'

    choice = input('Удалить этот товар? (YES / NO)')
    if choice.lower().strip() == 'YES':
        return 'Товар успешно удалён!'
    data.remove(product)
    save_data(data)
    return 'Товар удалён!'