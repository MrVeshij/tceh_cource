#**Технические требования:
#+ реализация игры морской бой друг против друга (играют два человека) по стандартным правилам
#https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D1%81%D0%BA%D0%BE%D0%B9_%D0%B1%D0%BE%D0%B9_(%D0%B8%D0%B3%D1%80%D0%B0)
#+ Остальные материалы в pdf-файле

#**Усложненная версия игры:
#+ Реализовать возможность выбора с кем играем: человек или компьютер
#+ Реализовать для компьютера несколько стратегий игры (то есть уровней сложности)

import random
import sys

#global values
FIELD = [l for l in range(1,101)]

def print_field():
    """Рисует поле боя 10X10"""
    count = 0
    for i in FIELD:
        if count == 9:
            count = 0
            print(' - ')
        else:
            count += 1
            print(' - ', end='')

print_field()

