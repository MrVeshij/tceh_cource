# Практическое задание:
#
# +1. Пользователь по GET запросу на адрес / получает
# сообщение: "Число загадано"
#
# +2. Пользователь по POST запросе на адрес /guess
# получает один из следующих результатов: ">", "<", "="
#
# +3. Если число угадано - загадываем новое число
#
# +4. Flask при старте сервера - устанавливает seed для
# random, генерирует случайное число для угадывания
#
# +5. Администратор задает seed для модуля рандом через
# переменную окружения FLASK_RANDOM_SEED
#
#
#
# О чем подумать?
# + Все пользователи угадывают одно число или каждый свое?
# + Можно ли считать количество попыток и количество угаданных чисел?
# + Как хранить данные между запросами?

# from flask import Flask
#
# app = Flask(__name__)
# app.config.update(
#     DEBUG = 'True'
# )
#
# @app.route('/',methods='GET','POST')
# def guess_number():
#     if method == 'GET':

#Вариант спизженный у Бориса Рубина (версия а)
#Написать усложненную версию кода от борьки рубина

from flask import Flask, request, url_for

import config

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators

import random,datetime
from os import environ


__author__ = 'PopovVladimir'


class Riddler():
    """Класс Riddler будет загадывать загадки"""
    __instance = None


    number = None


    def __new__(cls):
        if Riddler.__instance == None:
            Riddler.__instance = object.__new__(cls)
        return Riddler.__instance



    @classmethod
    def new_number(cls, limit):
        cls.number = random.randint(1,limit)
        print('Загадано число', cls.number)



class GuessForm(FlaskForm):
    riddle_number = DecimalField(label = 'Number is',validators=[validators.Required()])



app = Flask(__name__)
app.config.from_object(config)



@app.route('/', methods=['GET'])
def home():
    Riddler.new_number(100)
    return 'Загадано число от 1 до 100'

@app.route('/guess', methods=['POST'])
def guess():
    if Riddler.number is None:
        return 'Вы не загадали число'

    if request.method == 'POST':
        print(request.form,'that request.form')
        form = GuessForm(request.form)
        print(form.validate())

        if form.validate():
            user_number = form.riddle_number.data


            if user_number == Riddler.number:
                Riddler.new_number(100)
                return 'Вы угадали! Загадано новое число'
            elif user_number > Riddler.number:
                return 'Ваше число больше загаданного (>)'
            elif user_number < Riddler.number:
                return 'Ваше число меньше загаданного (<)'

        else:
            return str(form.errors)

    else:
        return url_for('home')



if __name__ == '__main__':
    seed_number = environ.get('ALIASES')

    if seed_number is None:
        print('FLASK_RANDOM_SEED is not assigned.Aborted!')
        exit()

    print('FLASK_RANDOM_SEED = ', seed_number)

    random.seed(seed_number)

    app.run()






































