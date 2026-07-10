#Impure functions : has side effects modifies external state
counter = 0
def impure_increment():
    global counter
    counter += 1
    return counter

print(impure_increment())

#print(impure_increment())  # Output: 1

def pure_increment(x):
    return x + 1

print(pure_increment(10))  # Output: 11
print(pure_increment(5))  # Output: 6