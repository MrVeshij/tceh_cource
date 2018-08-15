#введите путь до файла относительно текущий папки, проверьте существует ли такой файл, если да верните yes если нет no
#Посмотреть в видео (поискать) и записать реализацию от тех кто выполняет курс
from flask import Flask as f

app = f(__name__)

@app.route('/hm1/<somefile>')
def check_info(somefile):
    #read_file = open('/hm1/{}'.format(somefile))
    try:
        if somefile == 'sometext.txt':
            return 'yes'
        else:
            return 'no'
    except Exception:
        print('Error: file not finding')

if __name__ == '__main__':
    app.run()