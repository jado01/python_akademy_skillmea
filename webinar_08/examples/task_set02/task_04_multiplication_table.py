# Úloha 4 - Tabuľka násobkov (n x n)
# Zadaj n a vytvor tabuľku násobkov n x n.

# Sem napíš svoje riešenie:

n = 3

for row in range(1, n + 1):
    for column in range(1, n + 1):
        print(row * column, end=" ")
    print()