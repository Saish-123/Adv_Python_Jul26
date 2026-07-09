#First-Class Function
#1 Assigning a function to a variable
def say_hello(name):
    return f"Hello, {name}!"

#Assigning the function to a variable without parentheses
greet_function = say_hello
print(greet_function("Saish"))
print(say_hello("Saish"))

#2 Passing a function as an argument to another function
def apply_operation(func, value):
    return func(value)

def double(x):
    return x * 2
#passing different functions as arguments
print(apply_operation(double, 5))

#3 Returning a function from another function
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Using the returned function
double = make_multiplier(20)
print(double(2))  # Output: 40

#4 Storing functions in data structures
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y
}

print(operations['add'](10,5))
print(operations['subtract'](10,5))
print(operations['multiply'](10,5))