# импортируем библиотеку
import json

# словарь
data = {
    "name": "Ivan Ivanov",
    "age": "25"
}

# сериализуем словарь в JSON-структуру
json_string = json.dumps(data)

# распечатаем JSON-строку
print(json_string)
print(data)

print(type(json_string))
# <class 'str'>

# печатаем сериализованные данные
print(type(data))
# {"name": "Ivan Ivanov", "age": "25"}