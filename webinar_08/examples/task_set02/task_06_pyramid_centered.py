# Úloha 6 - Centrovaná (stredová) pyramída
# Zadaj n a vytvor centrovanú pyramídu z hviezdičiek.

# Sem napíš svoje riešenie:

n = 4

for row in range(1, n + 1):
    for space in range(n - row, 0, -1 ):
        print(" ", end="")
    for star in range(0, row * 2 - 1):
        print("*", end="")
    print()