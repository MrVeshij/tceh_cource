#+ Реализовать две функции: write_to_file(data) и read_file_data().
#Которые соотвественно: пишут данные в файл и читают данные из файла.

def write_to_file(file,content,mode):
    f = open(file,mode=mode)
    f.write(content)
    f.close()

write_to_file('text2.txt','SUPER','w')

def read_to_file(file):
    f = open(file)
    info = f.read()
    f.close()
    return info

print(read_to_file('text2.txt'))