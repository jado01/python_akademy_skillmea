# Úloha 1 - Spočítaj čísla od 1 do 10
# Použi for cyklus a vypočítaj súčet čísel od 1 po 10.
# Vystup: 55

#Sem napíš svoje riešenie:

numbers = range(1,11)

counter =0

for sum_numbers in numbers:
   counter += sum_numbers
print(counter)

# pomocovu while kod vyzera takto:

"""
number = 1

counter = 0

while number <= 10:
    counter += number
    number += 1
print(counter)
"""