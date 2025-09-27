# Úloha 6 - Počet slov dlhších ako 5 znakov
# Vytvor zoznam slov a vypíš počet tých, ktoré majú viac ako 5 znakov.
# slova = ["auto", "elektrina", "dom", "programovanie"]
# Vystup: 2

# Sem napíš svoje riešenie:

slova = ["auto", "elektrina", "dom", "programovanie"]

counter = 0
i = 0

while i < len(slova):
    if len(slova[i]) > 5:
        counter += 1
    i += 1
print(counter)

# for slovo in slova:
#     if len(slovo) > 5:
#         counter +=1
# print(counter)