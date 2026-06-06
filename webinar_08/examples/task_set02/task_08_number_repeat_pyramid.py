# Úloha 8 - Číselná pyramída s opakovaním čísla
# Zadaj n a vytvor pyramídu, kde sa v každom riadku opakuje číslo riadku.

# Sem napíš svoje riešenie:

n = 4

for row in range(1, n + 1):
    for column in range(0, row):
        print(row, end="")
    print()
