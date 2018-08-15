#Реализовать декоратор, который измеряет скорость выполнения функций.

import time

def time_line(funk):
    def inner():
        value_time_1 = time.clock()
        funk()
        value_time_2 =time.clock()
        time_work = value_time_2 - value_time_1
        print("Function work ", time_work)
    return inner

@time_line
def list_500():
    a = ([i for i in range(1,50000000)])

list_500()