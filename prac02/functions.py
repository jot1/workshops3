__author__ = 'Cue'
def square_number(num):
    return(num * num)
print(square_number(5))
"""
function to check whether the no is prime
"""
def is_prime(value):
    i = 2
    while i < value:
        remainder = value % i
        if remainder == 0:
            return False
        i += 1
    return True

is_prime(is_prime(5))

def celsius_to_fahrenheit(celsius):
		return celsius * 1.8 + 32.0

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
