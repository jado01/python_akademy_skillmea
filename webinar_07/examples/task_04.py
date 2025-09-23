# Úloha 4:
# Napíš program, ktorý vo vete nahradí malé písmeno "a" veľkým "A".

sentense = "Nahrad kazde 'a' velkym 'A'"

for letter in sentense:
    if letter == "a":
        print("A", end="")
    else:
        print(letter, end="")
