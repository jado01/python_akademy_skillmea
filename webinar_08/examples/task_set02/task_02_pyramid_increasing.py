# Úloha 2 - Stúpajúca pyramída z hviezdičiek
# Zadaj n a vypíš 'stúpajúcu' pyramídu.

# Sem napíš svoje riešenie:

n = 5

for row in range(1, n + 1):
    for column in range(0, row):
        print("*", end=" ")
    print()
   