# -------------------------------------------------------------------
# Темка:
# __getstate__
# __setstate__
# что означают эти методы в питон

# Метод __getstate__ является частью протокола сериализации в Python и используется при сериализации
# объектов с помощью модуля pickle. Когда объект сериализуется с помощью pickle.dump() или pickle.dumps(),
# метод __getstate__ вызывается у объекта для определения (состояния), которое должно быть сохранено.

# Обычно метод __getstate__ определяет, какие атрибуты объекта должны быть сериализованы. Он должен
# возвращать словарь, содержащий состояние объекта, которое нужно сохранить. Этот словарь будет передан
# в метод __setstate__ при десериализации объекта.

# Пример использования метода __getstate__:

# import pickle
#
#
# class MyClass:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __getstate__(self):
#         # Сохраняем только атрибут x
#         return {'x': self.x}
#
#     def __setstate__(self, state):
#         # Восстанавливаем состояние объекта (x) из переданного словаря
#         self.x = state['x']
#
#
# obj = MyClass(10, 20)
# sob = pickle.dumps(obj)
# print(sob)

# Результат:
# b'\x80\x04\x95%\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x07MyClass\x94\x93\x94)\x81\x94}\x94\x8c\x01x\
# x94K\nsb.'

# В этом примере метод __getstate__ определяет, что должен быть сохранен только атрибут (x) объекта MyClass,
# поэтому при сериализации будет сохранен только атрибут (x), а атрибут (y) будет проигнорирован.

# -------------------------------------------------------------------

# Что такое метод dump в Питон * * *

# Метод dump() в Python обычно используется для записи сериализованных данных в файл. Этот метод доступен в
# различных модулях Python, таких, как pickle, json, yaml и других.

# Например, в модуле pickle метод dump() используется для записи сериализованных объектов Python в файл:

# import pickle
#
# data = {'name': 'Alice', 'age': 30}
#
# # Открываем файл для записи бинарных данных
# with open('data.pkl', 'wb') as f:
#     pickle.dump(data, f)


# В этом примере объект data сериализуется с помощью pickle.dump() и сохраняется в файл data.pkl в бинарном формате.

# Аналогично, в модуле json метод dump() используется для записи сериализованных данных в файл в формате JSON:

# import json
#
# data = {'name': 'Bob', 'age': 25}
#
# # Открываем файл для записи данных в формате JSON
# with open('data.json', 'w') as f:
#     json.dump(data, f)


# Здесь объект data сериализуется с помощью json.dump() и сохраняется в файл data.json в формате JSON.

# Таким образом, метод dump() в Python обеспечивает запись сериализованных данных в файл, что позволяет
# сохранить данные для последующего использования.


# import json
#
#
# class CountryCapital:  # создадим класс, где мы все эти методы будет реализовывать
#     # @staticmethod
#     # def load(file_name):
#     #     # data = None
#     #     try:
#     #         data = json.load(open(file_name))
#     #     except FileNotFoundError:
#     #         data = {}
#     #     finally:
#     #         return data
#
#     @staticmethod  # Нам здесь проще и удобнее использовать статические методы, чтобы не создавать экземпляры
#     # класса. Мы можем просто обращаться к имени класса (CountryCapital.) и вызывать нужный нам метод
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()  # приводит к нижнему регистру
#         new_capital = input("Введите название столицы: ").lower()
#
#         data = CountryCapital.load(file_name)  # load - это метод или функция, используемая для загрузки
#         # данных о странах и их столицах из файла с указанным именем (file_name)
#         # Она выполняет чтение данных из файла и создание объекта (или объектов), представляющих эту информацию,
#         # которые затем могут быть использованы в программе.
#
#         data[new_country] = new_capital  # у нас есть словарь data{}, но нам нужно записать туда new_country -
#         # ключом, а new_capital - значением
#
#         with open(file_name, 'w') as f:  # 'w' - режим записи, создаем файл
#             json.dump(data, f, indent=2)  # dump - это функция из модуля json, которая используется для записи
#             # данных в файл в формате JSON.


# import requests
# ChatGPT
# requests - это модуль в Python, который предоставляет простой и удобный способ взаимодействия с веб-ресурсами.
# Он позволяет отправлять HTTP-запросы (например, GET, POST, PUT, DELETE и т.д.) и получать ответы от серверов.
# После того как вы импортируете модуль requests с помощью команды import requests, вы можете использовать его
# функциональность для выполнения различных HTTP-запросов. Например:

# import requests
#
# # Отправка GET-запроса
# response = requests.get('https://api.example.com/data')
#
# # Отправка POST-запроса с данными
# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://api.example.com/submit', data=payload)
#
# # Проверка успешности запроса и вывод ответа
# if response.status_code == 200:
#     print(response.text)
# else:
#     print('Ошибка:', response.status_code)
# В этом примере мы импортируем модуль requests и используем его для отправки GET- и POST-запросов на различные
# URL-адреса. Результаты запросов сохраняются в переменной response, и мы можем анализировать их,
# проверяя статус-коды и получая текст ответов.


# -------------------------------------------------------
# ДЗ №33 от 17.04.2024
# Задача:
# Нужно взять любой json объект (в json формате), к примеру, тот, который можно найти по данной
# ссылке - https://jsonplaceholder.typicode.com/todos и преобразовать его в формат csv (в Python)

# import requests  # Эта строка импортирует модуль requests, который используется для отправки HTTP-запросов
# # на сторонний ресурс
# import csv  # Эта строка импортирует модуль csv, который предоставляет функциональность для работы
# # с файлами в формате CSV
#
# # Загружаем данные из JSON-файла на стороннем ресурсе
# response = requests.get("https://jsonplaceholder.typicode.com/todos")  # Эта строка отправляет GET-запрос
# # по указанному URL-адресу, который возвращает данные в формате JSON. Полученный ответ сохраняется
# # в переменной response.
# todos = response.json()  # здесь мы преобразовываем полученные данные из формата JSON в Python-объекты.
# # Результат сохраняется в переменной (todos).
#
# # Открываем файл для записи в формате CSV
# with open("todos.csv", "w", newline='') as csvfile:  # Этот блок открывает файл "todos.csv" для записи
#     # ("w" - режим записи). Опция newline='' указывает, что при записи файл будет использовать пустую строку
#     # в качестве символа новой строки. Блок (with) гарантирует автоматическое закрытие файла после завершения
#     # работы с ним.
#     # Создаем объект для записи CSV
#     csv_writer = csv.writer(csvfile)  # Эта строка создает объект csv_writer, который предоставляет методы
#     # для записи данных в CSV-файл.
#
#     # Записываем заголовки столбцов
#     csv_writer.writerow(["userId", "id", "title", "completed"])  # Эта строка записывает первую строку в CSV-файл,
#     # содержащую заголовки столбцов: "userId", "id", "title" и "completed".
#
#     # Записываем данные из JSON в CSV
#     for todo in todos:  # Этот цикл перебирает каждую задачу из списка todos, который содержит данные из JSON.
#         csv_writer.writerow([todo["userId"], todo["id"], todo["title"], todo["completed"]])
# #  В этой строке записывается строка данных в CSV-файл. Каждая строка соответствует одной задаче.
# #  Значения из задачи извлекаются по ключам (userId, id, title, completed) и записываются в
# #  соответствующие столбцы CSV.
#
# print("Данные успешно записаны в файл todos.csv")
# # Эта строка выводит сообщение о том, что данные успешно записаны в файл "todos.csv".


# НАШ ПЕРВЫЙ КОД - НАШ ОБРАЗЕЦ!
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# -------------------------------------------------------
# ДЗ №33 от 17.04.2024
# Задача:
# User - С помощью языка Python реализовать парсинг данных из любого интернет ресурса с однотипными данными
# и сохранить их в формате csv

# Шаг 1: Импорт необходимых библиотек
# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# # requests: Эта библиотека используется для отправки HTTP-запросов к веб-сайтам и получения HTML-кода страницы.
# # BeautifulSoup: Это библиотека для парсинга HTML и извлечения данных из него.
# # csv: Эта библиотека позволяет нам работать с CSV-файлами, создавать и записывать данные в них.
#
#
# # Шаг 2: Функция для получения HTML-кода страницы
# def get_html(url):
#     response = requests.get(url)
#     return response.text
#
#
# # Эта функция принимает URL в качестве аргумента и использует библиотеку requests для отправки GET-запроса
# # к указанному URL. Затем она возвращает текст HTML-кода страницы.
#
# # Шаг 3: Функция для парсинга данных из HTML
# def parse(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     books = []
#     for book in soup.find_all('article', class_='product_pod'):
#         title = book.find('h3').find('a')['title']
#         price = book.find('p', class_='price_color').get_text()
#         books.append({'Title': title, 'Price': price})
#     return books
#
#
# # Шаг 4: Функция для сохранения данных в CSV
#
# def save_csv(data, path):
#     with open(path, 'w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['Title', 'Price']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for item in data:
#             writer.writerow(item)
#
#
# # Шаг 5: Основная функция
# def main():
#     url = 'http://books.toscrape.com/'
#     html = get_html(url)
#     data = parse(html)
#     save_csv(data, 'books.csv')
#
#
# if __name__ == '__main__':
#     main()
# -------------------------------------------------------




