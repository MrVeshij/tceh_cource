# mariamyzz
# https://gist.github.com/mariamyzz/1b65f182ac1e9ec58e1cdb2861d7dd02#file-read_and_write-py

# Реализовать следующую логику:
# получать при помощи requests данные сервиса
# https://jsonplaceholder.typicode.com/
# (сущность можно выбрать любую,
# например https://jsonplaceholder.typicode.com/comments),
# выводить в консоль все пары заголовки,
# сохранять полученный json в файл на диск

import requests
import json


def print_headers_and_save_json(url: str, filename):
    r = requests.get(url)

    headers_dict = dict(r.headers)
    for key, value in headers_dict.items():
        print(key+':', value)

    with open(filename, 'wb') as file:
        for chunk in r.iter_content(chunk_size=128):
            file.write(chunk)

print_headers_and_save_json('https://jsonplaceholder.typicode.com/comments',
                             'jsonplaceholdercomments.json')