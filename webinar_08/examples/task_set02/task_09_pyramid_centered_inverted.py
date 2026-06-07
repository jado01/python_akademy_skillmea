# Úloha 9 - Obrátená centrovaná pyramída
# Zadaj n a vytvor obrátenú centrovanú pyramídu.

# Sem napíš svoje riešenie:
n = 4

for row in range(n, 0, -1):
    for column in range(0, n - row):
        print(" ", end="")
    for star in range(row * 2 - 1, 0, -1):
        print("*", end="")
    print()