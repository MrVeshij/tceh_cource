from flask import Flask

app = Flask(__name__)

@app.route('/moststring/<string1>,<string2>,<string3>')
def home(string1,string2,string3):
    if len(string1) > len(string2) and len(string1) > len(string3):
        return 'most long string is ' + string1
    elif len(string2) > len(string1) and len(string2) > len(string3):
        return 'most long string is ' + string2
    elif len(string3) > len(string1) and len(string3) > len(string2):
        return 'most long string is ' + string3
    else:
        return 'Not happening'


if __name__ == '__main__':
    app.run()