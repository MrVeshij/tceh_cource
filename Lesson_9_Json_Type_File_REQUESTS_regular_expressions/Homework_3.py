#+ Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
#При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
#Ответить себе на вопрос удобно ли так делать?

import requests, re

def get_habr(url):
    r = requests.get(url)
    links = re.findall(r'href="(.*?)"', r.text, flags = re.IGNORECASE)
    return links

print(get_habr('https://habrahabr.ru/'))