# JSON - JavaScript Object Notation 
#Единый формат, хранения и передачи данных между компьютерами , серверами , приложениями и языками 
# програмирования через сеть интернет. 
# <Filenam>e.json # файл в формате json




# {
#     "id" : 1,
#     "author": "Ed Sheern",
#     "title": "Perfect",
#     "year": 2015

# } --- Это JSON
# наша задачDictionaryа научиться переводить данные JSON в Python 

#!!!!!!!!!!!!!

# JS == {}
# PY dict == {key: value}
# JSON == {key: value}



#Процессы Сериализации Дестериалтзации  данных 

# Сериализация(Запись данных в JSON) - Это перевод из Python в Json формат 

# DUMP -> метод записывает Python данные в файл в формате jSON, ПАРАЛЛЕЛЬНО СДЕЛАВ СЕРИАЛТЗАЦИИ 

# DUMPS - метод записывает Python данные в текст в формате Json, паралельно сделав сериализацию.

#Десериализация (Чтение данных из JSON) - это процесс перевода из JSONа в PY dict

#LOAD - МЕТОД КОТОРЫЙ СЧИТЫВАЕТ ФАЙЛ В ФОРМАТЕ JSON И переводит его в PY DICT
#LOADS - метод который считывает текст в формате JSON  переводит его  В PY dict


#-------------------------------------------------

# роцесс сериализации 

# import json

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'wife': False,
#     'children': None
# }

# print(dict_)
# print(type(dict_))
# json_text = json.dumps(dict_)

# print()
# print(json_text)
# print(type(json_text))

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

# with open('new.json', 'r') as file:
#     data = file.read()
#     print(data)

#---------------------------------------------------

#Процесс десериализации 

# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data)

# dict_ = json.loads(json_data)
# print(dict_)
# print(type(dict_))

# import json
# with open('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_)
#     print(type(dict_))

#--------------------------------------------

# from urllib.request import urlopen
# import json

# url = 'https://randomuser.me/api/'

# json_data = urlopen(url)

# # print(json_data)
# # print(type(json_data))

# dict_ = json.load(json_data)
# print(dict_)
# print(type(dict_))