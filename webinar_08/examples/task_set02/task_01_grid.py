# Úloha 1 - n x n mriežka hviezdičiek
# Zadaj n a vypíš štvorcovú mriežku n x n.

# Sem napíš svoje riešenie:

n = 3

for row in range(0, n):
    for column in range(0, n):
        print("*", end=" ")
    print()
