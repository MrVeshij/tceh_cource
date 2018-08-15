#+ Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
#(сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
#выводить в консоль все пары заголовки, сохранять полученный json в файл на диск

import requests
import json

def give_info(url, file):
    r = requests.get(url)

    headers_dict = dict(r.headers)
    for key, value in headers_dict.items():
        print(key,':',value,'\n')

    with open(file,'wb') as f:
        for i in r.iter_content(chunk_size=128):
            f.write(i)
give_info('https://www.pornhub.com/' , 'thatjson.json')


