def my_function():
    print('I am a function')

my_function()

print(my_function)
print('Functions are objects', isinstance(my_function, object))


test = my_function
test()

my_list = []
my_list.append(my_function)
print(my_list)

def call_passed_function(incoming):
    print('Calling!')
    incoming()
    print('Called!')

call_passed_function(my_function)

try:
    d = 2
    d()
except TypeError as e:
    print('It is not a function', e)

print(callable(len), callable(45),callable(callable))

def return_min_function():
    return min

test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)

