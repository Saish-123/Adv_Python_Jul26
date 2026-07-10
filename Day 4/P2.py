#Higher-order function: Functions that either take other functions as arguments or return a function as a result are called higher-order functions. In Python, functions are first-class citizens, which means they can be passed around and used as arguments just like any other object (string, int, float, list, and so on).

from sys import prefix


def apply_twice(func, value):
    return func(func(value))

def add_two(x):
    return x + 2

print(apply_twice(add_two, 10))  # Output: 14

#2. return a function
def make_logger(prefix):
    def logger(message):
        print(f"{prefix}: {message}")
    return logger

info_logger = make_logger("INFO")
info_logger("System Started") 
