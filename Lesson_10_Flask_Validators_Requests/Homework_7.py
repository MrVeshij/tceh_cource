# 5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files.
# Файлы можно туда положить любые текстовые. А если такого нет - 404.

from flask import Flask
import os


app = Flask(__name__)
app.config.update(
    DEBUG = True
)

@app.route('/serve/<path:filename>')
def learn_path(filename):
    if not os.path.exists('./files/' + filename):
        return '404. File not found'
    else:
        file = open('./files/' + filename)
        info = file.read()
        file.close()
        return info

if __name__ == '__main__':
    app.run()
