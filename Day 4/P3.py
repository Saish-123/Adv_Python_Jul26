#Immutability 

#Mutable
my_list=[1,2,3]
my_list[0]=10
print(my_list)  # Output: [10, 2, 3]

#Immutable
my_tuple=(1,2,3)
my_tuple[0]=10  # This will raise an error because tuples are immutable

def pure_process(data):
    return data + (4,5,6)

original = (1,2,3)

processed = pure_process(original)
print(processed)  
print(original)  # Output: (1, 2, 3)