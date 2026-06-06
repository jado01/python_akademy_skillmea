# Úloha 3 - Stúpajúce čísla v tvare pyramídy
# Zadaj n a vypíš čísla od 1 po číslo riadku.

# Sem napíš svoje riešenie:

n = 4

for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()
