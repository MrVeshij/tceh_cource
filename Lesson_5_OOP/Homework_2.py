# *ЗАДАЧА 2:
# Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

class Printer():
    def log(self, *values):
        print(values)


class FormattedPrinter():
    def formattext(self, *values):
        print('**********************')
        print(values)
        print('**********************')



objprint = Printer()
objprint2 = FormattedPrinter()

objprint2.formattext('Rupert')
