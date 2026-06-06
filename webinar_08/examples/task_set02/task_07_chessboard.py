# Úloha 7 - Šachovnica n x n
# Zadaj n a vytvor šachovnicu zo striedania * a medzier.

# Sem napíš svoje riešenie:

n = 4

for row in range(0, n):
    if row % 2 == 0:
        print(" ", end="")
    for column in range(0, 2):

        print("*", end="")
    print()
    