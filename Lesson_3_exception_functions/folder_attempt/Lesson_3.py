# from builtins import ZeroDivisionError
#
# try:
#     print(1/1)
# except ZeroDivisionError:
#     print('0!')
# finally:
#     print('I will be called in the end!')


def my_function(input_var1, input_var2):
    print(input_var1, input_var2)
    return input_var1 + input_var2

first_call = my_function(1, 1)
print(first_call)

second_call = my_function(1, 123)
print(second_call)

def my_function(var1, var2, var3):
    print("No way I'm using this: {},{},{}" .format(var1, var2, var3))

new_call = my_function(1, 2, 3)
print(new_call)

