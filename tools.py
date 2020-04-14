"""
An assorted collection of fun tools!
"""
from random import randint

def is_even(n):
    # Returns true if n is even
    return n % 2 == 0

def randn():
    # Returns a random integer
    return randint(0, 100)