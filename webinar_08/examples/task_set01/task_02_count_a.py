# Úloha 2 - Spočítaj počet písmen v slove
# Zadaj slovo do premennej a pomocou cyklu vypíš počet výskytov písmena 'a'.
# slovo = "banan"
# Vystup: 2

# Sem napíš svoje riešenie:


# word = "banan"

# counter = 0

# for letter in word:
#     if letter == "a":
#         counter += 1
    
# print(counter)

# kod s while cyklom:

word = "banan"

counter = 0
i = 0

while i < len(word):
    if word[i] == "a":
        counter += 1
    i += 1
print(counter)
    
