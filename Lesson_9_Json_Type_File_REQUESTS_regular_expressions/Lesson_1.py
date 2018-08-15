

def read_file(filename):
    try:
        f = open(filename)
        content = f.read()
    finally:
        f.close()

    return content

print(read_file("text.txt"))


def write_to_file(filename, content, mode = 'w'):
    with open(filename, mode = mode) as f:
        f.write(content)

content = '\nI like play with big tits'
write_to_file('test.txt',content,'w')

print(read_file('test.txt'))

