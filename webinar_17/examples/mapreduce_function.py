from functools import reduce

numbers = [2, 3, 4, 5, 6]

def return_power_of_two(num):
    return num*num

print(list(map(return_power_of_two, numbers))) # vrati [4, 9, 16, 25, 36]
print([return_power_of_two(num) for num in numbers]) # vrati [4, 9, 16, 25, 36]

print(list(map(lambda num: num*num, numbers))) # to iste ako vyzsie, vrati [4, 9, 16, 25, 36]

def is_even(num):
    return num % 2 == 0

print(list(filter(is_even, numbers)))
print(list(filter(lambda num: num % 2 ==0, numbers))) # to iste ako o riadok vyzsie s vyuzitim funkcie lamda 

def reduce_sum(a, b):
    return a + b

print(reduce(reduce_sum, numbers))
print(reduce(lambda a,b: a + b, numbers)) # to iste ako o riadok vyzsie s vyuzitim funkcie lamda, v tomto pripade ma dva parametre "a" a "b"