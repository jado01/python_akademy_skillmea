import random
import sys

print("Vitaj v hre: Uhádni číslo!")
print("Napíš q kedykoľvek pre koniec.")

    
while True:
    secret = random.randint(1,10)
    pokusy = 0

    while True:
        guess_input = input("Tipni si číslo 1-10 (alebo q pre koniec): ")
        if guess_input == "q":
            print("Dakujem, program konci")
            sys.exit(0)

        try:
            guess = int(guess_input)
        except ValueError:
            print("to nie je číslo")
            continue
        if guess < 1:
            print("Zadal si číslo menšie ako 1! Zadaj prosím číslo od 1 do 10")
            continue
        elif guess > 10:
            print("Zadal si číslo väčšie ako 10! Zadaj prosím číslo od 1 do 10")
            continue

        pokusy += 1

        if guess < secret:
            print("Moje číslo je väčšie")
        elif guess > secret:
            print("Moje číslo je menšie")
        else:
            if pokusy == 1:
                print(f"Výborne, trafil si na prvý krát!")
            else:
                print(f"Výborne, trafil si po {pokusy} pokusoch.")
            break
    
    while True:
        c = input("Chces pokracovat? y/n ").strip().lower()
        if c in {"y", "yes", "áno", "ano"}:
            print("OK, nová hra.")
            break
        if c in {"n", "no", "nie"}:
            print("OK, končím. 👋")
            sys.exit(0)
        print("Nerozumiem. Zadaj prosím y/n.")