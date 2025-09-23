# Úloha 3:
# Použi vnorený for cyklus.
# Vypíš všetky kombinácie dvojíc čísel od 0 po 5.

numbers = range(0,6)
for first in numbers:
    for second in numbers:
        print(f"{[first, second]}")