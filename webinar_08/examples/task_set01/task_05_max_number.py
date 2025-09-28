# Úloha 5 - Nájdite najväčšie číslo v zozname
# Pomocou cyklu najdi najväčšie číslo v zozname bez použitia funkcie max().
# cisla = [3, 9, 1, 14, 7]
# Vystup: Najväčšie číslo je 14

# Sem napíš svoje riešenie:

# RIESENIE S FOR CYKLOM:

# numbers = [3, 9, 1, 14, 7]

# max_number = numbers[0]

# for number in numbers:
#     if number > max_number:
#         max_number = number
# print(max_number)

# RIESENIE S WHILE CYKLOM:

numbers = [3, 9, 1, 14, 7]

max_number = numbers[0]
index = 0

while index < len(numbers):
    if numbers[index] > max_number:
        max_number = numbers[index]
    index += 1
print(max_number)

