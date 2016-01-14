import operator

def get_array_product(number_array):
    if not number_array:
        raise ValueError("number_array is empty. It should contain at least one number")
    return reduce(operator.mul, number_array)
