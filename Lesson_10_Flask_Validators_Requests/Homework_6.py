# 4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля.
# Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают.
# Возрващать пользователю json вида:
#  "status" - 0 или 1 (если ошибка валидации),
#  "errors" - список ошибок, если они есть,
#  или пустой список.


#Вариант наполовину спизженный
#Непонятны следующие моменты: form.data? ValidationError?form.errors?
from flask import Flask,request,jsonify
from flask_wtf import FlaskForm, Form
from wtforms import StringField, validators, ValidationError

def check_password(form,field):
    if form.data['first_password'] != form.data['second_password']:
        raise ValidationError('Пароли не совпадают')



class ContactForm(FlaskForm):
    email = StringField('Email', validators=[
        validators.Length(min=8,max=60),
        validators.Required()
    ])

    first_password = StringField('Password', validators=[
        validators.Length(min=6,max=50),
        validators.Required()
    ])

    second_password = StringField('Confirm Password', validators=[
        validators.Length(min=6,max=50),
        validators.Required(),
        check_password
    ])

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY = 'SECRET KEY MUST BE SECRET',
    WTF_CSRF_ENABLED = False
)

@app.route('/form/user', methods=['GET','POST'])
def req_pas():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        status_output = {0: 'Проверка пройдена', 1: 'Ошибка валидации'}
        #print(form.validate())

        if form.validate():
            status_check = jsonify(status_output[0])
            return status_check
        else:
            status_check = jsonify(status_output[1])
            error_list = jsonify(form.errors)
            # print(user_form.errors)
            return status_check and error_list

    elif request.method == 'GET':
        print('It\'s GET request')

    return 'Done!'

if __name__ == '__main__':
    app.run()












#Пытался запили свой вариант основываясь на validators из документации, но нихуя не вышло
from flask import Flask,request,jsonify
from flask_wtf import FlaskForm, Form
from wtforms import StringField, validators
import wtforms

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[
        validators.Length(min=8,max=60),
        validators.Required()
    ])

    first_password = wtforms.PasswordField('Password', validators=[
        validators.Length(min=6,max=50),
        validators.Required()
    ])

    second_password = wtforms.PasswordField('Confirm Password', validators=[
        validators.Length(min=6,max=50),
        validators.Required(),
        #validators.EqualTo(first_password)
    ])

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY = 'SECRET KEY MUST BE SECRET',
    WTF_CSRF_ENABLED = False
)

@app.route('/form/user', methods=['GET','POST'])
def req_pas():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return 'Ok', 200
        else:
            return 'not ok', 400

    elif request.method == 'GET':
        return 'It\' GET request', 200

if __name__ == '__main__':
    app.run()

