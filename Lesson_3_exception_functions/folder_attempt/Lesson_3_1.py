def sum_numb(*numbers):
    print(numbers)
    max = 0

    for i in numbers:
        max += i

    return max


print(sum_numb(1,2,3,4,5,6,7,8))

