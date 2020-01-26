"""Формирование файла с пользователями и книгами с помощью менеджера контекста"""
import json
import csv

# Открываем файл с книгами и сохраняем каждую строку в список
with open('books.csv') as file_with_books:
    book_list = []
    csv_reader = csv.DictReader(file_with_books)
    for row in csv_reader:
        book_list.append(row)

# Сохраняем полученный список в словарь json
with open('books_list.json', 'w') as books_json:
    json.dump(book_list, books_json, sort_keys=True, indent=4)

# Открываем файлы с книгами и пользователями, и сохраняем в новый json файл результаты по нужному шаблону
with open('books_list.json') as books_list_json:
    json_data_books = json.load(books_list_json)
    for book in json_data_books:
        with open('users.json', 'r') as user_json:
            users_json_data = json.load(user_json)
            output_result = []
            for item in users_json_data:
                output_result.append(
                    {'name': item["name"], 'gender': item["gender"], 'address': item["address"], 'books': book})

    with open('users_and_books_result.json', 'w') as users_books_result:
        json.dump(output_result, users_books_result, sort_keys=True, indent=4)
