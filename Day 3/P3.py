#Syntax
#lambda parameter_list: expression
#Lambda Functions
add_lambda = lambda x, y: x + y
print(add_lambda(10, 50))  # Output: 60
subtract_lambda = lambda x, y: x - y
print(subtract_lambda(50, 10))  # Output: 40

#Lambda with filter()
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

#Lambda with map()
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Lambda as a key in dictionary
Students = {
    'name': 'Saish',
    'age': 20,
    'grade': lambda x: grade(x)
}
print(Students['name'])  # Output: Saish
print(Students['age'])
print(Students['grade'](87))