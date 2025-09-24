# Úloha 3 - Vypíš len kladné čísla
# Vytvor zoznam s číslami (kladné aj záporné) a vypíš iba tie, ktoré sú väčšie ako nula.
# cisla = [-3, 0, 4, 1, -5, 7]
# Vystup: 4, 1, 7

# Sem napíš svoje riešenie:

# numbers = [-3, 0, 4, 1, -5, 7]
# positive_numbers = []

# for number in numbers:
#     if number > 0:
#         print(number, end = ", ")


#priklad doplneny o vysledok v hranatych zatvorkach - zoznam kladnych cisel
# numbers = [-3, 0, 4, 1, -5, 7]
# positive_numbers = []

# for number in numbers:
#     if number > 0:
#         positive_numbers.append(number)
# print(positive_numbers)

#priklad s while:

numbers = [-3, 0, 4, 1, -5, 7]

i = 0
positive_numbers = []

while i < len(numbers):
    if numbers[i] > 0:
        positive_numbers.append(numbers[i])
    i += 1
print(positive_numbers)
    