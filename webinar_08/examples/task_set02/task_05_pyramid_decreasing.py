# Úloha 5 - Opatrná pyramída z hviezdičiek (klesajúca)
# Zadaj n a vypíš 'klesajúcu' pyramídu.

# Sem napíš svoje riešenie:

n = 5

for row in range(5, 0, -1):
    for column in range(0, row):
        print("*", end=" ")
    print()
