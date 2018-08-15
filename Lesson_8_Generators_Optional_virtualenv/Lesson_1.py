def cities():
    cities = ['Moscow',
              'Tula',
              'Krasnodar',
              'Perm',
              'Vladivostok']
    return iter(cities)


if __name__ == '__main__':

    a = cities()

    while True:
        try:
            print(next(a))
        except StopIteration:
            break



