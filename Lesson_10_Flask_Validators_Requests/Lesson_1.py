from flask import Flask

app = Flask(__name__)

@app.route('/math/<numb1>,<numb2>')
def home(numb1, numb2):
    sum = int(numb1) + int(numb2)
    sum = str(sum)
    return 'hello, user: ' + sum

if __name__ == '__main__':
    app.run()