"""
    Prime numbers are only divisible by itself and 1
    Ex: 2,3,5,7,11,13,17,19,23,29,etc.
"""


def is_prime(number):
    for i in range(2, number - 1):
        if number % i == 0:
            return "Is not a prime number"

    return "Is a prime number"


n = int(input("Check this number:\t"))
print(is_prime(number=n))

"""
    Check if number is divisible by all previous numbers except 1
    If divisible by none, return prime
    If at least divisible by 1, return not prime
"""
