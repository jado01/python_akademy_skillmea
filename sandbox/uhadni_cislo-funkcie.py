import random
import sys

def ask_continue():
    while True:
        answer = input("Chceš pokračovať? (y/n): ").strip().lower()
        if answer in {"y", "yes", "áno", "ano"}:
            return True
        elif answer in {"n", "no", "nie"}:
            return False
        else:
            print("Nerozumiem. Zadaj prosím y alebo n.")


def play_round():
    secret = random.randint(1, 10)
    pokusy = 0

    while True:
        guess_input = input("Tipni si číslo 1-10 (alebo q pre koniec): ").strip().lower()

        # možnosť okamžite skončiť celú hru
        if guess_input == "q":
            print("Ďakujem, program končí. 👋")
            sys.exit(0)

        # pokus o prevod na číslo
        try:
            guess = int(guess_input)
        except ValueError:
            print("To nie je číslo.")
            continue

        # kontrola rozsahu
        if guess < 1:
            print("Zadal si číslo menšie ako 1! Zadaj prosím číslo od 1 do 10.")
            continue
        elif guess > 10:
            print("Zadal si číslo väčšie ako 10! Zadaj prosím číslo od 1 do 10.")
            continue

        pokusy += 1

        # porovnanie s tajným číslom
        if guess < secret:
            print("Moje číslo je väčšie.")
        elif guess > secret:
            print("Moje číslo je menšie.")
        else:
            if pokusy == 1:
                print("Výborne, trafil si na prvý krát!")
            else:
                print(f"Výborne, trafil si po {pokusy} pokusoch.")
            break  # koniec tejto jednej hry

    # keď hra skončí úspechom, spýtame sa, či chce pokračovať
    return ask_continue()


while True:
    # play_round() vráti True = chce hrať znova
    # play_round() vráti False = nechce hrať znova
    if not play_round():
        print("Ďakujem, že si hral! 👋")
        break

