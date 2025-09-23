# Úloha 6:
# Použi while cyklus.
# Napíš program, ktorý vypíše ľubovoľný text 10-krát.

text = input("Zadaj text: ")
number = int(input("Zadaj pocet opakovani: "))

counter = 0

while counter < number:
    counter += 1
    print(text)
print("Python je proste super :)")
