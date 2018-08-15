#2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму
# from flask import Flask
#Во втором примере непонятные синтаксические связи

#
# app = Flask(__name__)
#
# @app.route('/math/<numb1>,<numb2>')
# def home(numb1, numb2):
#     sum = int(numb1) + int(numb2)
#     sum = str(sum)
#     return 'hello, user: ' + sum
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask

app = Flask(__name__)

@app.route('/math/<int:numb1>/<int:numb2>')
def home(numb1,numb2):
    sum = numb1 + numb2
    return sum

if __name__ == '__main__':
    app.run()

# from flask import Flask, request
#
# app = Flask(__name__)
#
#
# @app.route('/sum/<int:first>/<int:second>')
# def calc_sum(first, second):
#     return 'sum = {}'.format(first + second)
#
# if __name__ == '__main__':
#     app.run()
