import math

def multiply_list(numbers):

    result = math.prod(numbers)
    return result

numbers_list = [2, 3, 5, 7, 11]
result = multiply_list(numbers_list)

print(result)
