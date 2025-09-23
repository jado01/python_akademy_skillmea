# Úloha 2:
# Vypíš iba párne čísla od 0 po 50 pomocou for cyklu a podmienky if.

numbers = range(0, 51)
for even in numbers:
    if even % 2 == 0:
        print(even)
